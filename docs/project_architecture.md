# Project Architecture

## Project Name

Pharma Analytics Platform

---

# Business Problem

Pharmaceutical sales and commercial teams require a centralized analytics platform to analyze:

* Product performance
* Territory performance
* Sales representative effectiveness
* Healthcare provider interactions
* Inventory availability

Data exists across multiple operational systems and must be consolidated into a single analytics platform.

---

# High Level Architecture

Source APIs
↓
Python Extraction Layer
↓
Apache Airflow
↓
AWS S3 Bronze Layer
↓
Snowflake BRONZE Schema
↓
dbt Silver Models
↓
Snowflake SILVER Schema
↓
dbt Gold Models
↓
Snowflake GOLD Schema
↓
Semantic Marts
↓
Power BI Dashboards

---

# Source Systems

## CRM API

Provides:

* Accounts
* Interactions

Example Data:

* Hospitals
* Clinics
* Pharmacies
* Sales Activities

---

## ERP API

Provides:

* Orders
* Revenue
* Quantity Sold

---

## Product Master API

Provides:

* Product Details
* Brand Information
* Product Categories

---

## Inventory API

Provides:

* Daily Inventory Levels
* Stock Availability

---

# Data Extraction Layer

Technology:

* Python

Responsibilities:

* Connect to source APIs
* Extract daily data
* Validate API responses
* Store raw files in AWS S3

Python Libraries:

* requests
* pandas
* boto3
* snowflake-connector-python

---

# Workflow Orchestration

Technology:

* Apache Airflow

Responsibilities:

* Schedule daily jobs
* Monitor pipeline execution
* Trigger Snowflake loads
* Execute dbt transformations
* Run data quality checks

Daily Pipeline Flow:

1. Extract source data
2. Store files in AWS S3
3. Load Snowflake BRONZE tables
4. Execute dbt Silver models
5. Execute dbt Gold models
6. Run validation checks
7. Refresh reporting datasets

---

# Bronze Layer

Technology:

* AWS S3
* Snowflake BRONZE Schema

Purpose:

Store source data exactly as received.

Tables:

* accounts
* products
* sales_rep
* orders
* interactions
* inventory

Characteristics:

* Immutable
* Historical
* Auditable
* Minimal Transformations

---

# Silver Layer

Technology:

* dbt
* Snowflake

Purpose:

Create standardized and reusable dimensions.

Tables:

* dim_account
* dim_product
* dim_sales_rep
* dim_date

Transformations:

* Deduplication
* Null Handling
* Data Standardization
* Surrogate Key Generation
* Data Validation

---

# Gold Layer

Technology:

* dbt
* Snowflake

Purpose:

Create analytics-ready fact tables.

Tables:

## fact_orders

Measures:

* quantity
* revenue

---

## fact_interactions

Measures:

* interaction_count

---

## fact_inventory

Measures:

* stock_quantity

---

# Semantic Layer

Purpose:

Provide business-friendly data marts for reporting.

---

## Territory Insights Mart

KPIs:

* Total Revenue
* Total Orders
* Total Interactions
* Active Accounts

---

## Product Performance Mart

KPIs:

* Revenue by Product
* Quantity Sold
* Product Growth Rate

---

## Account Insights Mart

KPIs:

* Revenue by Account
* Interaction Count
* Product Adoption

---

# Reporting Layer

Technology:

* Power BI

Dashboards:

* Executive Dashboard
* Territory Dashboard
* Product Dashboard
* Account Dashboard

---

# Data Quality Checks

Implemented using dbt tests.

Checks:

* not_null
* unique
* relationships
* accepted_values

Examples:

* Product must exist in Product Master.
* Account must exist in Account Dimension.
* Revenue cannot be negative.
* Quantity cannot be negative.

---

# Future Enhancements

* Incremental Processing
* Change Data Capture (CDC)
* Slowly Changing Dimensions (SCD Type 2)
* Real-Time Data Processing
* Forecasting Models
* Data Observability Framework

---

# Key Benefits

* Scalable architecture
* Enterprise-grade analytics
* Reusable business models
* Improved data quality
* Faster reporting performance
* Centralized reporting platform
