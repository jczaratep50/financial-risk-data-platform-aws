# Financial Risk Analytics Platform on AWS

## Project Overview

This project demonstrates the design and implementation of an end-to-end cloud-native data platform for credit risk analytics. It simulates the data ecosystem of a financial institution by generating synthetic loan portfolio data, processing it through an automated ETL pipeline, and enabling business-oriented analytics using AWS cloud services.

The solution was built to showcase practical experience with AWS services commonly used in production environments while applying software engineering best practices such as modular ETL design, schema enforcement, partitioned storage, workflow orchestration, and reusable analytics.

## Business Problem

Financial institutions manage large credit portfolios composed of thousands of customers, loans, payment transactions, and risk indicators. Raw operational data is often distributed across multiple systems and cannot be queried efficiently for business analysis without prior processing.

This project addresses that challenge by transforming raw CSV datasets into optimized analytical tables that support portfolio monitoring, credit risk assessment, and executive reporting.

## Solution Overview

The platform automates the complete analytics workflow for a synthetic credit risk portfolio.

Raw CSV datasets are stored in Amazon S3, where an AWS Glue ETL job processes and transforms the data into optimized Parquet files. AWS Step Functions orchestrates the pipeline by executing the ETL process and automatically triggering a Glue Crawler to update the Data Catalog. Finally, Amazon Athena provides a serverless SQL layer for portfolio analysis, while Power BI consumes the analytical data to build business dashboards and executive KPIs.

## Solution Architecture

The following diagram illustrates the end-to-end architecture of the platform, from raw data ingestion to business intelligence and analytics.

<img width="442" height="672" alt="diagram_architecture" src="https://github.com/user-attachments/assets/562a52c7-4210-4ba7-ba56-cacec767f333" />

## Technology Stack

| Category             | Technologies                            |
| -------------------- | --------------------------------------- |
| Programming Language | Python                                  |
| Data Processing      | PySpark, AWS Glue                       |
| Cloud Platform       | Amazon Web Services (AWS)               |
| Storage              | Amazon S3                               |
| Orchestration        | AWS Step Functions                      |
| Metadata Catalog     | AWS Glue Data Catalog, AWS Glue Crawler |
| Query Engine         | Amazon Athena                           |
| Data Format          | CSV, Parquet                            |
| Dashboard            | Power BI                                |

## Repository Structure

```text
financial-risk-analytics-platform/
│
├── architecture/        # Solution architecture diagrams
├── athena/              # Business-oriented SQL queries
├── images/              # Architecture and execution screenshots
├── sample_data/         # Synthetic datasets used in the project
├── src/                 # Python scripts (data generation and AWS Glue ETL)
└── README.md
```

## Data Pipeline

The platform follows a fully automated data pipeline.

1. Synthetic financial datasets are generated using **Python**.
2. Raw CSV files are uploaded to **Amazon S3**.
3. AWS Glue processes the raw data with **PySpark**, applying predefined schemas and **data transformations**.
4. Processed datasets are stored in **Parquet** format **partitioning** for optimized analytical performance.
5. **AWS Step Functions** orchestrates the **ETL workflow** by executing the **Glue job** and triggering the **Glue Crawler**.
6. The **Glue Crawler** updates the **AWS Glue Data Catalog**.
7. **Amazon Athena** provides a serverless **SQL** layer for portfolio analysis.
8. **Power BI** connects to the analytical layer to create business dashboards and executive **KPIs**.

## SQL Analytics

Amazon Athena is used as the analytical query engine for the processed datasets. The project includes a set of business-oriented SQL queries that support portfolio monitoring and credit risk analysis.

Implemented analyses include:

| Query                        | Business Purpose                 |
| ---------------------------- | -------------------------------- |
| Executive Portfolio Overview | Portfolio KPIs                   |
| Credit Risk Analysis         | Product-level risk metrics       |
| Portfolio Composition        | Segment analysis                 |
| Top Riskiest Loans           | Identify highest expected losses |
| Collections & Delinquency    | Payment performance              |

## Dashboard

The project includes an interactive Power BI dashboard connected directly to Amazon Athena through the AWS Glue Data Catalog.

The dashboard provides an executive view of the credit portfolio, allowing users to monitor key risk indicators, portfolio composition, payment performance, and the largest credit exposures through interactive filters.

### Dashboard Highlights

- Executive KPIs (Total Loans, Customers, EAD, Expected Loss, Default Rate and Average Interest Rate)
- Portfolio analysis by product and customer segment
- Portfolio risk distribution by risk category
- Payment status analysis
- Top credit exposures ranked by Expected Loss
- Interactive filtering by Product, Customer Segment and Loan Status

<img width="1420" height="801" alt="dashboard" src="https://github.com/user-attachments/assets/666bb696-4650-4550-a081-b6bb8d79d0d9" />

## Business Insights

The analytical layer developed in this project provides several insights into the simulated credit portfolio:

- The portfolio consists of approximately **24.8K active loans** distributed across **8.2K customers**, indicating multiple credit products per customer.

- Corporate loans represent the largest exposure (EAD) within the portfolio, concentrating most of the financial risk.

- Although the overall **Default Rate is only 1.92%**, the portfolio accumulates an **Expected Loss of approximately 845 million**, highlighting the impact of high-value exposures.

- Corporate customers generate the highest Expected Loss among all customer segments, suggesting that exposure concentration has a greater impact on portfolio risk than default frequency alone.

- The portfolio is primarily composed of **Moderate** and **Low** risk loans, while High and Very High risk categories account for only a small proportion of the total portfolio.

- Approximately **90% of all payments are completed successfully**, indicating healthy payment behavior across most borrowers.




