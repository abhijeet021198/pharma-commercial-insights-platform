# Source System Design

## Project Overview

The Pharma Analytics Platform ingests data from multiple operational systems including CRM, ERP, Product Master, HR, and Inventory systems. These source datasets are loaded into the Bronze layer and transformed through the Medallion Architecture to support analytics and reporting.

---

# Source Systems

| Source System               | Data Domain            |
| --------------------------- | ---------------------- |
| CRM                         | Accounts, Interactions |
| ERP                         | Orders                 |
| Product Master              | Products               |
| HR System                   | Sales Representatives  |
| Inventory Management System | Inventory              |

---

# Accounts Source

**Table Name:** accounts

| Column Name  | Data Type | Description                |
| ------------ | --------- | -------------------------- |
| account_id   | VARCHAR   | Unique account identifier  |
| account_name | VARCHAR   | Account name               |
| account_type | VARCHAR   | Hospital, Clinic, Pharmacy |
| city         | VARCHAR   | City                       |
| state        | VARCHAR   | State                      |
| region       | VARCHAR   | Region                     |

### Sample Record

| account_id | account_name    | account_type | city   | state       | region |
| ---------- | --------------- | ------------ | ------ | ----------- | ------ |
| ACC001     | Apollo Hospital | Hospital     | Mumbai | Maharashtra | West   |

---

# Products Source

**Table Name:** products

| Column Name  | Data Type | Description        |
| ------------ | --------- | ------------------ |
| product_id   | VARCHAR   | Product identifier |
| product_name | VARCHAR   | Medicine name      |
| brand        | VARCHAR   | Brand name         |
| category     | VARCHAR   | Product category   |

### Sample Record

| product_id | product_name | brand | category   |
| ---------- | ------------ | ----- | ---------- |
| PROD001    | Stelara      | J&J   | Immunology |

---

# Sales Representative Source

**Table Name:** sales_rep

| Column Name | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| rep_id      | VARCHAR   | Representative identifier |
| rep_name    | VARCHAR   | Representative name       |
| territory   | VARCHAR   | Assigned territory        |

### Sample Record

| rep_id | rep_name     | territory |
| ------ | ------------ | --------- |
| REP001 | Rahul Sharma | West      |

---

# Orders Source

**Table Name:** orders

| Column Name | Data Type     | Description          |
| ----------- | ------------- | -------------------- |
| order_id    | VARCHAR       | Order identifier     |
| account_id  | VARCHAR       | Account reference    |
| product_id  | VARCHAR       | Product reference    |
| rep_id      | VARCHAR       | Sales representative |
| order_date  | DATE          | Order date           |
| quantity    | NUMBER        | Units sold           |
| revenue     | DECIMAL(18,2) | Revenue amount       |

### Sample Record

| order_id | account_id | product_id | rep_id | order_date | quantity | revenue |
| -------- | ---------- | ---------- | ------ | ---------- | -------- | ------- |
| ORD001   | ACC001     | PROD001    | REP001 | 2026-01-15 | 50       | 250000  |

---

# Interactions Source

**Table Name:** interactions

| Column Name      | Data Type | Description            |
| ---------------- | --------- | ---------------------- |
| interaction_id   | VARCHAR   | Interaction identifier |
| account_id       | VARCHAR   | Account reference      |
| rep_id           | VARCHAR   | Sales representative   |
| interaction_date | DATE      | Interaction date       |
| interaction_type | VARCHAR   | Call, Visit, Email     |

### Sample Record

| interaction_id | account_id | rep_id | interaction_date | interaction_type |
| -------------- | ---------- | ------ | ---------------- | ---------------- |
| INT001         | ACC001     | REP001 | 2026-01-10       | Visit            |

---

# Inventory Source

**Table Name:** inventory

| Column Name    | Data Type | Description             |
| -------------- | --------- | ----------------------- |
| product_id     | VARCHAR   | Product reference       |
| inventory_date | DATE      | Inventory snapshot date |
| stock_quantity | NUMBER    | Available stock         |

### Sample Record

| product_id | inventory_date | stock_quantity |
| ---------- | -------------- | -------------- |
| PROD001    | 2026-01-15     | 5000           |

---

# Data Flow

Source Systems
↓
Bronze Layer (Raw Data)
↓
Silver Layer (Cleaned & Standardized Data)
↓
Gold Layer (Business Facts & Dimensions)
↓
Semantic Layer
↓
Power BI Dashboards

---

# Key Business Use Cases

1. Analyze product sales performance.
2. Track healthcare provider interactions.
3. Monitor inventory availability.
4. Measure territory performance.
5. Generate executive dashboards and KPIs.
