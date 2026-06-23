# Data Model Design

## Dimension Tables

### DIM_ACCOUNT

Stores account information.

Columns:
- account_key
- account_id
- account_name
- account_type
- city
- state
- region

### DIM_PRODUCT

Stores medicine information.

Columns:
- product_key
- product_id
- product_name
- brand
- category

### DIM_DATE

Stores date hierarchy.

Columns:
- date_key
- full_date
- month
- quarter
- year

### DIM_SALES_REP

Stores representative information.

Columns:
- rep_key
- rep_id
- rep_name
- territory

## Fact Tables

### FACT_ORDERS

Grain:
One order line per product per account per day.

Measures:
- quantity
- revenue

### FACT_INTERACTIONS

Grain:
One interaction event.

Measures:
- interaction_count

### FACT_INVENTORY

Grain:
One product inventory snapshot per day.

Measures:
- stock_quantity
