-- Create Schema

CREATE SCHEMA IF NOT EXISTS BRONZE;

----------------------------------------------------
-- ACCOUNTS
----------------------------------------------------

CREATE OR REPLACE TABLE BRONZE.ACCOUNTS (
    ACCOUNT_ID VARCHAR(50),
    ACCOUNT_NAME VARCHAR(255),
    ACCOUNT_TYPE VARCHAR(100),
    CITY VARCHAR(100),
    STATE VARCHAR(100),
    REGION VARCHAR(100)
);

----------------------------------------------------
-- PRODUCTS
----------------------------------------------------

CREATE OR REPLACE TABLE BRONZE.PRODUCTS (
    PRODUCT_ID VARCHAR(50),
    PRODUCT_NAME VARCHAR(255),
    BRAND VARCHAR(255),
    CATEGORY VARCHAR(100)
);

----------------------------------------------------
-- SALES REPRESENTATIVES
----------------------------------------------------

CREATE OR REPLACE TABLE BRONZE.SALES_REP (
    REP_ID VARCHAR(50),
    REP_NAME VARCHAR(255),
    TERRITORY VARCHAR(100)
);

----------------------------------------------------
-- ORDERS
----------------------------------------------------

CREATE OR REPLACE TABLE BRONZE.ORDERS (
    ORDER_ID VARCHAR(50),
    ACCOUNT_ID VARCHAR(50),
    PRODUCT_ID VARCHAR(50),
    REP_ID VARCHAR(50),
    ORDER_DATE DATE,
    QUANTITY NUMBER(10,0),
    REVENUE NUMBER(18,2)
);

----------------------------------------------------
-- INTERACTIONS
----------------------------------------------------

CREATE OR REPLACE TABLE BRONZE.INTERACTIONS (
    INTERACTION_ID VARCHAR(50),
    ACCOUNT_ID VARCHAR(50),
    REP_ID VARCHAR(50),
    INTERACTION_DATE DATE,
    INTERACTION_TYPE VARCHAR(50)
);

----------------------------------------------------
-- INVENTORY
----------------------------------------------------

CREATE OR REPLACE TABLE BRONZE.INVENTORY (
    PRODUCT_ID VARCHAR(50),
    INVENTORY_DATE DATE,
    STOCK_QUANTITY NUMBER(10,0)
);
