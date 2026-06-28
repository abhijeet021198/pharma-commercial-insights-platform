# Project Architecture

## Project Name

**Pharma Commercial Insights Platform**

---

# Project Status

| Phase                 | Status         |
| --------------------- | -------------- |
| Foundation Setup      | ✅ Completed    |
| Bronze Layer          | ✅ Completed    |
| Silver Layer          | ✅ Completed    |
| Gold Layer            | 🔄 In Progress |
| Airflow Orchestration | ⏳ Planned      |
| AWS S3 Integration    | ⏳ Planned      |
| Power BI Dashboard    | ⏳ Planned      |

---

# Business Problem

Pharmaceutical sales and commercial teams require a centralized analytics platform to analyze:

* Product performance
* Territory performance
* Sales representative effectiveness
* Healthcare provider interactions
* Inventory availability

Operational data is distributed across multiple systems and requires standardization before it can be used for analytics and reporting.

The objective of this platform is to build a scalable, modern Data Engineering solution that transforms raw operational data into trusted business-ready datasets.

---

# High Level Architecture

```text
CSV Files + OpenFDA API
            │
            ▼
     Python Extraction Layer
            │
            ▼
   Reusable Bronze Loader
            │
            ▼
 Snowflake BRONZE Schema
            │
            ▼
   dbt Bronze Staging Models
            │
            ▼
 Snowflake SILVER Schema
   (Dimensions & Facts)
            │
            ▼
    dbt GOLD Business Models
            │
            ▼
 Snowflake GOLD Schema
            │
            ▼
     Power BI Dashboards
```

---

# Current Repository Structure

```text
pharma-commercial-insights-platform/

├── data/
│   ├── accounts.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── inventory.csv
│   ├── interactions.csv
│   ├── sales_rep.csv
│   └── openfda_drugs.csv
│
├── python/
│   ├── extract/
│   ├── load/
│   └── utils/
│
├── dbt/
│   └── pharma_dbt/
│       ├── models/
│       │   ├── bronze/
│       │   ├── silver/
│       │   └── gold/
│       ├── macros/
│       └── tests/
│
└── docs/
```

---

# Source Systems

## Internal Business Data

Provides:

* Customer Accounts
* Products
* Orders
* Inventory
* Sales Representatives
* Customer Interactions

## External Data Source

### OpenFDA API

Provides:

* Drug Information
* Product Metadata
* Regulatory Reference Data

---

# Data Extraction Layer

### Technology

* Python
* Pandas
* Snowflake Connector
* OpenFDA REST API

### Responsibilities

* Read source CSV files
* Extract OpenFDA data
* Validate source data
* Load Bronze tables using reusable ingestion framework
* Perform row count validation

---

# Bronze Layer

### Technology

* Python
* Snowflake

### Purpose

Store raw source data with minimal transformation.

### Tables

* ACCOUNTS
* PRODUCTS
* ORDERS
* INVENTORY
* INTERACTIONS
* SALES_REP

### Characteristics

* Raw business data
* Reloadable
* Auditable
* Minimal transformations

---

# Bronze Staging Layer (dbt)

Purpose:

Standardize raw Bronze tables before dimensional modeling.

### Models

* STG_ACCOUNTS
* STG_PRODUCTS
* STG_ORDERS
* STG_INVENTORY
* STG_INTERACTIONS
* STG_SALES_REP

Responsibilities:

* Column standardization
* Consistent naming
* Clean source abstraction

---

# Silver Layer

### Technology

* dbt
* Snowflake

Purpose:

Create reusable dimensional models following Kimball Star Schema principles.

## Dimension Tables

* DIM_ACCOUNT
* DIM_PRODUCT
* DIM_SALES_REP
* DIM_DATE

Features:

* Surrogate Keys
* Business Keys
* Standardized Attributes
* Reusable Dimensions

---

## Fact Tables

### FACT_ORDERS

Measures:

* Quantity
* Revenue

Dimensions:

* Account
* Product
* Sales Representative
* Date

---

### FACT_INVENTORY

Measures:

* Stock Quantity

Dimensions:

* Product
* Date

---

### FACT_INTERACTIONS

Measures:

* Interaction Type

Dimensions:

* Account
* Sales Representative
* Date

---

# Star Schema

```text
                 DIM_ACCOUNT
                      │
                      │
DIM_PRODUCT ── FACT_ORDERS ── DIM_SALES_REP
                      │
                 DIM_DATE

DIM_PRODUCT ─ FACT_INVENTORY ─ DIM_DATE

DIM_ACCOUNT ─ FACT_INTERACTIONS ─ DIM_SALES_REP
                      │
                 DIM_DATE
```

---

# Data Quality Framework

Implemented using dbt Generic Tests.

Current Status:

* ✅ Unique Tests
* ✅ Not Null Tests
* ✅ Relationship Tests

Project Status:

* 34 Tests Implemented
* 34 Tests Passing

Validation includes:

* Primary key uniqueness
* Mandatory fields
* Referential integrity
* Foreign key validation

---

# Engineering Decisions

Current implementation follows:

* Medallion Architecture
* Kimball Star Schema
* Surrogate Keys
* Lookup Joins
* LEFT JOIN strategy for preserving business events
* dbt Generic Testing Framework

---

# Gold Layer (Next Phase)

Business-ready analytical models.

Planned Models:

* ACCOUNT_INSIGHTS
* PRODUCT_PERFORMANCE
* TERRITORY_INSIGHTS

These models will aggregate Silver layer data into reusable business KPIs for reporting.

---

# Reporting Layer

Technology

* Power BI (Planned)

Planned Dashboards

* Executive Dashboard
* Product Performance Dashboard
* Territory Dashboard
* Account Dashboard

---

# Future Enhancements

* Apache Airflow Orchestration
* AWS S3 Data Lake Integration
* Incremental dbt Models
* Slowly Changing Dimensions (SCD Type 2)
* Snowflake Streams & Tasks
* CI/CD Pipeline
* Data Observability
* Automated Deployment

---

# Key Benefits

* End-to-End Modern Data Engineering Pipeline
* Medallion Architecture Implementation
* Enterprise Star Schema Design
* Reusable dbt Transformation Framework
* Automated Data Quality Validation
* Modular and Scalable Architecture
* Analytics-Ready Data Models
* Portfolio-Ready Real-World Project
