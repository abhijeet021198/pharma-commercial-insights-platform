# Source to Target Mapping (STM)

## Purpose

This document defines how source system data is transformed and loaded into the Pharma Analytics Platform using the Medallion Architecture.

---

# Account Dimension Mapping

## Source

accounts

## Target

dim_account

| Source Column | Target Column | Transformation Rule          |
| ------------- | ------------- | ---------------------------- |
| account_id    | account_id    | Direct Mapping               |
| account_name  | account_name  | Trim Leading/Trailing Spaces |
| account_type  | account_type  | Direct Mapping               |
| city          | city          | Proper Case                  |
| state         | state         | Upper Case                   |
| region        | region        | Upper Case                   |
| N/A           | account_key   | Surrogate Key Generated      |

---

# Product Dimension Mapping

## Source

products

## Target

dim_product

| Source Column | Target Column | Transformation Rule     |
| ------------- | ------------- | ----------------------- |
| product_id    | product_id    | Direct Mapping          |
| product_name  | product_name  | Trim Spaces             |
| brand         | brand         | Direct Mapping          |
| category      | category      | Direct Mapping          |
| N/A           | product_key   | Surrogate Key Generated |

---

# Sales Representative Dimension Mapping

## Source

sales_rep

## Target

dim_sales_rep

| Source Column | Target Column | Transformation Rule     |
| ------------- | ------------- | ----------------------- |
| rep_id        | rep_id        | Direct Mapping          |
| rep_name      | rep_name      | Trim Spaces             |
| territory     | territory     | Upper Case              |
| N/A           | rep_key       | Surrogate Key Generated |

---

# Date Dimension Mapping

## Source

Derived from Order Date, Interaction Date and Inventory Date

## Target

dim_date

| Source Column | Target Column | Transformation Rule |
| ------------- | ------------- | ------------------- |
| order_date    | full_date     | Direct Mapping      |
| full_date     | month         | Extract Month       |
| full_date     | quarter       | Extract Quarter     |
| full_date     | year          | Extract Year        |
| N/A           | date_key      | YYYYMMDD Format     |

---

# Orders Fact Mapping

## Source

orders

## Target

fact_orders

| Source Column | Target Column | Transformation Rule  |
| ------------- | ------------- | -------------------- |
| account_id    | account_key   | Lookup DIM_ACCOUNT   |
| product_id    | product_key   | Lookup DIM_PRODUCT   |
| rep_id        | rep_key       | Lookup DIM_SALES_REP |
| order_date    | date_key      | Lookup DIM_DATE      |
| quantity      | quantity      | Direct Mapping       |
| revenue       | revenue       | Direct Mapping       |

---

# Interactions Fact Mapping

## Source

interactions

## Target

fact_interactions

| Source Column    | Target Column     | Transformation Rule  |
| ---------------- | ----------------- | -------------------- |
| account_id       | account_key       | Lookup DIM_ACCOUNT   |
| rep_id           | rep_key           | Lookup DIM_SALES_REP |
| interaction_date | date_key          | Lookup DIM_DATE      |
| interaction_id   | interaction_count | Count(1)             |

---

# Inventory Fact Mapping

## Source

inventory

## Target

fact_inventory

| Source Column  | Target Column  | Transformation Rule |
| -------------- | -------------- | ------------------- |
| product_id     | product_key    | Lookup DIM_PRODUCT  |
| inventory_date | date_key       | Lookup DIM_DATE     |
| stock_quantity | stock_quantity | Direct Mapping      |

---

# Data Quality Rules

1. Remove duplicate records based on business keys.
2. Reject records with null primary identifiers.
3. Standardize territory names.
4. Standardize state values.
5. Validate revenue values greater than zero.
6. Validate quantity values greater than zero.
7. Ensure product references exist in Product Master.
8. Ensure account references exist in Account Master.

---

# Surrogate Key Strategy

| Dimension     | Surrogate Key |
| ------------- | ------------- |
| DIM_ACCOUNT   | ACCOUNT_KEY   |
| DIM_PRODUCT   | PRODUCT_KEY   |
| DIM_SALES_REP | REP_KEY       |
| DIM_DATE      | DATE_KEY      |

Surrogate keys are generated in the Silver Layer and used by all Gold Fact Tables.

---

# Medallion Architecture Flow

Source Systems
↓
Bronze Layer
↓
Data Validation
↓
Silver Dimensions
↓
Gold Fact Tables
↓
Semantic Layer
↓
Power BI Dashboards
