# Pharma Commercial Insights Semantic Layer Platform

## Project Overview

The objective of this project is to design and implement a modern Data Engineering and Semantic Layer platform for a pharmaceutical organization using Snowflake, dbt, Airflow, Python, and SQL.

The platform will consolidate data from multiple operational systems, transform it using a Medallion Architecture (Bronze → Silver → Gold), and expose trusted business metrics through a governed Semantic Layer.

The solution aims to provide a single source of truth for commercial analytics, territory insights, sales performance, interaction effectiveness, distributor performance, and inventory reporting.

---

# Business Problem

Pharmaceutical organizations operate multiple systems for managing:

* Customer Accounts
* Product Catalogs
* Orders and Sales
* Sales Representative Interactions
* Inventory Management
* Territory Operations

As data grows across systems, business users face several challenges:

* KPI definitions vary across reports
* Business logic is duplicated across dashboards
* Analysts spend excessive time writing SQL
* Territory performance is difficult to measure consistently
* Revenue and interaction metrics are not standardized
* Inventory insights are delayed

The organization requires a centralized analytics platform that provides trusted, reusable business metrics and enables self-service analytics.

---

# Business Objectives

The platform should enable stakeholders to answer the following questions.

## Sales Analytics

* What is the total revenue by month, quarter, and year?
* Which medicines generate the highest revenue?
* Which products are growing or declining?
* What are the sales trends across regions?

## Territory Analytics

* Which territories are performing best?
* Which regions require attention?
* How do sales vary across territories?

## Interaction Analytics

* Are sales representative interactions influencing sales?
* Which interaction channels are most effective?
* What is the relationship between engagement and revenue?

## Distributor Analytics

* Which distributors contribute the most revenue?
* Which distributors are underperforming?
* How has distributor performance changed over time?

## Inventory Analytics

* Which products frequently go out of stock?
* What is the inventory turnover rate?
* What inventory risks exist across regions?

---

# Source Systems

## CRM System

Stores customer and account information.

### Entity

Accounts

### Example Attributes

* Account ID
* Account Name
* Account Type
* Region
* Territory
* State
* City

---

## Order Management System

Stores medicine sales transactions.

### Entity

Orders

### Example Attributes

* Order ID
* Account ID
* Product ID
* Quantity
* Revenue
* Order Date

---

## Sales Interaction System

Stores customer engagement information.

### Entity

Interactions

### Example Attributes

* Interaction ID
* Account ID
* Representative ID
* Interaction Type
* Interaction Date

---

## Product Master System

Stores medicine information.

### Entity

Products

### Example Attributes

* Product ID
* Product Name
* Brand
* Category
* Product Line

---

## Inventory Management System

Stores inventory snapshots and stock availability.

### Entity

Inventory

### Example Attributes

* Product ID
* Warehouse
* Stock Quantity
* Snapshot Date

---

# Solution Architecture

## Bronze Layer (Raw)

Purpose:

Store source data exactly as received.

Characteristics:

* Immutable
* Historical
* Auditable
* Supports replay and recovery

Tables:

* accounts_raw
* orders_raw
* interactions_raw
* products_raw
* inventory_raw

---

## Silver Layer (Standardized)

Purpose:

Clean, validate, and standardize source data.

Transformations:

* Null handling
* Data type standardization
* Deduplication
* Data quality validation
* Business rule enforcement

Models:

* stg_accounts
* stg_orders
* stg_interactions
* stg_products
* stg_inventory

---

## Gold Layer (Business Ready)

Purpose:

Create analytics-ready datasets using dimensional modeling.

### Dimension Tables

* dim_account
* dim_product
* dim_date
* dim_region
* dim_territory
* dim_sales_rep

### Fact Tables

* fact_orders
* fact_interactions
* fact_inventory
* fact_territory_insights

---

# Semantic Layer

Purpose:

Provide centralized KPI definitions and reusable business metrics.

Benefits:

* Consistent reporting
* Reduced duplication of business logic
* Self-service analytics
* Trusted KPI calculations

---

# Key Business KPIs

## Revenue Metrics

### Total Revenue

Revenue generated across all products and territories.

### Revenue Growth

Month-over-Month and Year-over-Year growth.

### Product Revenue

Revenue by product category and brand.

---

## Territory Metrics

### Territory Revenue

Revenue contribution by territory.

### Territory Growth

Growth trends across territories.

### Territory Ranking

Top and bottom performing territories.

---

## Interaction Metrics

### Interaction Count

Number of customer engagements.

### Interaction Effectiveness

Revenue generated per interaction.

### Engagement Trends

Interaction activity over time.

---

## Inventory Metrics

### Inventory Turnover

Sales compared against average inventory.

### Stock-Out Rate

Frequency of inventory shortages.

### Inventory Health

Overall inventory availability.

---

# Data Quality Framework

Data quality will be implemented using dbt tests.

Examples:

* Unique keys
* Not null validations
* Accepted values
* Referential integrity checks

Examples:

* Orders must reference valid Accounts
* Products must have unique Product IDs
* Revenue values cannot be negative

---

# Orchestration Strategy

Apache Airflow will orchestrate end-to-end workflows.

Pipeline Flow:

Source Extraction
→ Bronze Load
→ Silver Transformations
→ Gold Transformations
→ Semantic Layer Refresh
→ Dashboard Refresh

Features:

* Scheduling
* Retry Handling
* Monitoring
* Dependency Management

---

# Incremental Processing Strategy

Snowflake Streams and Tasks will be used for Change Data Capture (CDC).

Benefits:

* Process only changed records
* Reduce compute costs
* Improve pipeline efficiency
* Support near real-time analytics

---

# Reporting Layer

Business users will consume data through dashboards and reports.

Potential Tools:

* Power BI
* Tableau
* Snowflake Dashboards

---

# Expected Outcomes

* Single Source of Truth
* Governed Semantic Layer
* Consistent KPI Definitions
* Improved Data Quality
* Faster Analytics Delivery
* Self-Service Reporting
* Enhanced Commercial Insights
* Better Territory Planning
* Improved Inventory Visibility

---

# Technology Stack

* Snowflake
* SQL
* dbt
* Apache Airflow
* Python
* Power BI
* GitHub
* Medallion Architecture
* Semantic Layer Design
* Dimensional Modeling
