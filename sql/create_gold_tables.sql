-- Create Schema

CREATE SCHEMA IF NOT EXISTS GOLD;

----------------------------------------------------
-- FACT_ORDERS
----------------------------------------------------

CREATE OR REPLACE TABLE GOLD.FACT_ORDERS (
    ACCOUNT_KEY NUMBER,
    PRODUCT_KEY NUMBER,
    REP_KEY NUMBER,
    DATE_KEY NUMBER,
    QUANTITY NUMBER(10,0),
    REVENUE NUMBER(18,2)
);

----------------------------------------------------
-- FACT_INTERACTIONS
----------------------------------------------------

CREATE OR REPLACE TABLE GOLD.FACT_INTERACTIONS (
    ACCOUNT_KEY NUMBER,
    REP_KEY NUMBER,
    DATE_KEY NUMBER,
    INTERACTION_COUNT NUMBER(10,0)
);

----------------------------------------------------
-- FACT_INVENTORY
----------------------------------------------------

CREATE OR REPLACE TABLE GOLD.FACT_INVENTORY (
    PRODUCT_KEY NUMBER,
    DATE_KEY NUMBER,
    STOCK_QUANTITY NUMBER(10,0)
);
