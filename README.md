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
