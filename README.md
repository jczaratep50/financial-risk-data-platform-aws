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

## Architecture

