import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, BooleanType, DateType
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Native logger of glue
logger = glueContext.get_logger()

# Constants
BUCKET_NAME = 'financial-risk-data-platform-jczp-2026'

CONFIG = {
    'storage': {
        'bucket': BUCKET_NAME, 
        'raw_path': f"s3://{BUCKET_NAME}/raw/",
        'processed_path': f"s3://{BUCKET_NAME}/processed/"
    }, 
    'datasets': {
        'customers': {}, 
        'products': {}, 
        'loans': {'partition': 'origination_date'}, 
        'payments': {'partition': 'payment_date'},
        'risk_metrics': {'partition': 'calculation_date'}
    }
}

# Schemas
PRODUCTS_SCHEMA = StructType([
    StructField('product_id', StringType(), False), 
    StructField('product_name', StringType(), False), 
    StructField('secured', BooleanType(), False), 
    StructField('product_category', StringType(), False), 
    StructField('currency', StringType(), False), 
    StructField('max_term_months', IntegerType(), False), 
    StructField('max_amount', DoubleType(), False)
])

CUSTOMERS_SCHEMA = StructType([
    StructField('customer_id', StringType(), False), 
    StructField('segment', StringType(), False), 
    StructField('age', IntegerType(), False), 
    StructField('gender', StringType(), False), 
    StructField('state', StringType(), False), 
    StructField('occupation', StringType(), False), 
    StructField('registration_date', DateType(), False), 
    StructField('annual_income', DoubleType(), False)
])

LOANS_SCHEMA = StructType([
    StructField('loan_id', StringType(), False), 
    StructField('customer_id', StringType(), False), 
    StructField('product_id', StringType(), False), 
    StructField('origination_date', DateType(), False), 
    StructField('maturity_date', DateType(), False), 
    StructField('original_amount', DoubleType(), False), 
    StructField('outstanding_balance', DoubleType(), False), 
    StructField('interest_rate', DoubleType(), False), 
    StructField('term_months', IntegerType(), False), 
    StructField('payment_frequency', StringType(), False), 
    StructField('collateral_value', DoubleType(), True),
    StructField('loan_status', StringType(), False),
    StructField('loan_to_income_ratio', DoubleType(), False)
])

PAYMENTS_SCHEMA = StructType([
    StructField('payment_id', StringType(), False), 
    StructField('loan_id', StringType(), False), 
    StructField('installment_number', IntegerType(), False), 
    StructField('payment_date', DateType(), False), 
    StructField('scheduled_amount', DoubleType(), False), 
    StructField('actual_amount', DoubleType(), False), 
    StructField('days_past_due', IntegerType(), False), 
    StructField('payment_status', StringType(), False)
])

RISK_METRICS_SCHEMA = StructType([
    StructField('loan_id', StringType(), False), 
    StructField('calculation_date', DateType(), False), 
    StructField('pd', DoubleType(), False), 
    StructField('lgd', DoubleType(), False), 
    StructField('ead', DoubleType(), False), 
    StructField('expected_loss', DoubleType(), False), 
    StructField('risk_rating', StringType(), False), 
    StructField('default_flag', BooleanType(), False)
])

SCHEMAS = {
    "customers": CUSTOMERS_SCHEMA,
    "products": PRODUCTS_SCHEMA,
    "loans": LOANS_SCHEMA,
    "payments": PAYMENTS_SCHEMA,
    "risk_metrics": RISK_METRICS_SCHEMA,
}

# Functions
def read_dataset(dataset_name):
    
    logger.info(f"Reading dataset {dataset_name}")
    
    try:
    
        df = spark.read.csv(
            f"{CONFIG['storage']['raw_path']}{dataset_name}/{dataset_name}.csv", 
            header = True, sep = ',', 
            schema = SCHEMAS[dataset_name]
        )
        
        logger.info(f"Dataset {dataset_name} loaded succesfully")
        
        return df
        
    except Exception as e:
        
        logger.error(f"Error reading dataset '{dataset_name}': {str(e)}")
        raise


def transform_dataset(df, dataset_name):
    
    dataset_config = CONFIG['datasets'][dataset_name]
    
    if 'partition' in dataset_config:
    
        partition_columns = dataset_config['partition']
        partition_prefix = partition_columns.replace("_date", "")
        
        df = (
            df
            .withColumn(f"{partition_prefix}_year", F.year(F.col(partition_columns)))
            .withColumn(f"{partition_prefix}_month", F.month(F.col(partition_columns)))
        )
    
    return df
    
def write_dataset(df, dataset_name):
    
    processed_route = f"{CONFIG['storage']['processed_path']}{dataset_name}/"
    dataset_config = CONFIG['datasets'][dataset_name]
    
    logger.info(f"Writing datasets: {dataset_name}")
    logger.info(f"Output path: {processed_route}")
    
    if 'partition' in dataset_config.keys():
        
        # Data Parameters
        partition_columns = dataset_config['partition'].replace("_date", "")
        year_column = f"{partition_columns}_year"
        month_column = f"{partition_columns}_month"
        
        # Writing
        df.write.mode('overwrite').partitionBy(year_column, month_column).parquet(processed_route)
                
    else:
    
        df.write.mode("overwrite").parquet(processed_route)
    
    logger.info(f"Dataset: '{dataset_name}' written succesfully.")
    

# Read datasets
spark_datasets = {}

for dataset_name in CONFIG['datasets']:
    spark_datasets[dataset_name] = read_dataset(dataset_name)
    
# Transform datasets
transformed_datasets = {}

for dataset_name, df in spark_datasets.items():
    transformed_datasets[dataset_name] = transform_dataset(df, dataset_name)
    
# Writing datasets
for dataset_name, df in transformed_datasets.items():
    write_dataset(df, dataset_name)

job.commit()