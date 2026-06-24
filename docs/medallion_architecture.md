# Medallion Architecture Design

## Project Overview

The Pharma Analytics Platform is designed using the Medallion Architecture pattern to support scalable, governed, and analytics-ready data processing.

The platform ingests data from multiple operational systems, stores raw data in the Bronze layer, performs transformations in the Silver layer, creates business-ready datasets in the Gold layer, and exposes semantic marts for reporting and analytics.

---

# Architecture Flow

Source Systems
↓
Apache Airflow
↓
AWS S3 (Bronze Layer)
↓
Snowflake BRONZE Schema
↓
dbt Transformations
↓
Snowflake SILVER Schema
↓
dbt Business Models
↓
Snowflake GOLD Schema
↓
Semantic Layer
↓
Power BI Dashboards

---

# Technology Stack

| Layer           | Technology     |
| --------------- | -------------- |
| Orchestration   | Apache Airflow |
| Programming     | Python         |
| Cloud Storage   | AWS S3         |
| Data Warehouse  | Snowflake      |
| Transformation  | dbt            |
| Query Language  | SQL            |
| Reporting       | Power BI       |
| Version Control | GitHub         |

---

# Bronze Layer

## Purpose

Store raw source data exactly as received from operational systems.

The Bronze layer serves as the system of record and preserves historical source data for auditing and reprocessing.

---

## Storage Location

AWS S3

Snowflake Schema:
BRONZE

---

## Tables

### accounts

Stores account information from CRM.

Columns:

* account_id
* account_name
* account_type
* city
* state
* region

---

### products

Stores medicine information from Product Master.

Columns:

* product_id
* product_name
* brand
* category

---

### sales_rep

Stores sales representative information from HR systems.

Columns:

* rep_id
* rep_name
* territory

---

### orders

Stores order transactions from ERP systems.

Columns:

* order_id
* account_id
* product_id
* rep_id
* order_date
* quantity
* revenue

---

### interactions

Stores healthcare provider interactions.

Columns:

* interaction_id
* account_id
* rep_id
* interaction_date
* interaction_type

---

### inventory

Stores inventory snapshots.

Columns:

* product_id
* inventory_date
* stock_quantity

---

# Silver Layer

## Purpose

Clean and standardize source data while applying data quality rules and generating reusable dimensions.

Snowflake Schema:
SILVER

Transformation Tool:
dbt

---

## Dimension Tables

### dim_account

Business Key:

* account_id

Attributes:

* account_key
* account_id
* account_name
* account_type
* city
* state
* region

---

### dim_product

Business Key:

* product_id

Attributes:

* product_key
* product_id
* product_name
* brand
* category

---

### dim_sales_rep

Business Key:

* rep_id

Attributes:

* rep_key
* rep_id
* rep_name
* territory

---

### dim_date

Attributes:

* date_key
* full_date
* month
* quarter
* year

---

## Silver Layer Transformations

### Data Cleansing

* Remove duplicate records
* Trim spaces
* Standardize text formats
* Handle null values

### Data Validation

* Validate mandatory fields
* Validate revenue values
* Validate quantity values
* Validate reference keys

### Data Enrichment

* Generate surrogate keys
* Generate date hierarchy
* Standardize territory mappings
* Standardize regional mappings

---

# Gold Layer

## Purpose

Provide analytics-ready fact tables optimized for reporting and dashboard consumption.

Snowflake Schema:
GOLD

Transformation Tool:
dbt

---

## fact_orders

### Grain

One order line per product per account per day.

### Measures

* quantity
* revenue

### Foreign Keys

* account_key
* product_key
* rep_key
* date_key

---

## fact_interactions

### Grain

One interaction event.

### Measures

* interaction_count

### Foreign Keys

* account_key
* rep_key
* date_key

---

## fact_inventory

### Grain

One product inventory snapshot per day.

### Measures

* stock_quantity

### Foreign Keys

* product_key
* date_key

---

# Semantic Layer

## Purpose

Create business-friendly marts used by analysts, business users, and Power BI dashboards.

---

## Territory Insights Mart

### KPIs

* Total Revenue
* Total Orders
* Total Interactions
* Active Accounts

### Dimensions

* Territory
* Sales Representative
* Date

---

## Product Performance Mart

### KPIs

* Revenue by Product
* Quantity Sold
* Product Growth Rate

### Dimensions

* Product
* Territory
* Date

---

## Account Insights Mart

### KPIs

* Revenue by Account
* Interaction Count
* Product Adoption

### Dimensions

* Account
* Product
* Date

---

# Airflow Orchestration

Apache Airflow is used to orchestrate end-to-end data pipelines.

Daily Workflow:

1. Extract source files.
2. Load files to AWS S3.
3. Load raw data into Snowflake BRONZE schema.
4. Execute dbt Silver models.
5. Execute dbt Gold models.
6. Run data quality checks.
7. Refresh Power BI datasets.

---

# dbt Transformation Framework

dbt is used for:

* Data cleansing
* Data standardization
* Business transformations
* Fact table generation
* Data quality testing
* Documentation generation

Common dbt Tests:

* unique
* not_null
* accepted_values
* relationships

---

# Snowflake Data Warehouse Design

Schemas:

BRONZE

* accounts
* products
* sales_rep
* orders
* interactions
* inventory

SILVER

* dim_account
* dim_product
* dim_sales_rep
* dim_date

GOLD

* fact_orders
* fact_interactions
* fact_inventory

MART

* territory_insights
* product_performance
* account_insights

---

# Benefits of the Architecture

1. Scalable cloud-native design.
2. Separation of bronze and curated data.
3. Reusable business dimensions.
4. Faster reporting performance.
5. Strong data governance.
6. Easier troubleshooting and auditing.
7. Enterprise-ready analytics platform.

---

# Future Enhancements

1. Slowly Changing Dimensions (SCD Type 2).
2. Change Data Capture (CDC).
3. Incremental dbt Models.
4. Data Quality Monitoring Framework.
5. Real-Time Streaming Pipelines.
6. Predictive Analytics Models.
7. Forecasting and Demand Planning.
