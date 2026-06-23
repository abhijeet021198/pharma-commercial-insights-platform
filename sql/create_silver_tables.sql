-- Create Schema

CREATE SCHEMA IF NOT EXISTS SILVER;

----------------------------------------------------
-- DIM_ACCOUNT
----------------------------------------------------

CREATE OR REPLACE TABLE SILVER.DIM_ACCOUNT (
    ACCOUNT_KEY NUMBER AUTOINCREMENT,
    ACCOUNT_ID VARCHAR(50),
    ACCOUNT_NAME VARCHAR(255),
    ACCOUNT_TYPE VARCHAR(100),
    CITY VARCHAR(100),
    STATE VARCHAR(100),
    REGION VARCHAR(100)
);

----------------------------------------------------
-- DIM_PRODUCT
----------------------------------------------------

CREATE OR REPLACE TABLE SILVER.DIM_PRODUCT (
    PRODUCT_KEY NUMBER AUTOINCREMENT,
    PRODUCT_ID VARCHAR(50),
    PRODUCT_NAME VARCHAR(255),
    BRAND VARCHAR(255),
    CATEGORY VARCHAR(100)
);

----------------------------------------------------
-- DIM_SALES_REP
----------------------------------------------------

CREATE OR REPLACE TABLE SILVER.DIM_SALES_REP (
    REP_KEY NUMBER AUTOINCREMENT,
    REP_ID VARCHAR(50),
    REP_NAME VARCHAR(255),
    TERRITORY VARCHAR(100)
);

----------------------------------------------------
-- DIM_DATE
----------------------------------------------------

CREATE OR REPLACE TABLE SILVER.DIM_DATE (
    DATE_KEY NUMBER,
    FULL_DATE DATE,
    MONTH NUMBER,
    QUARTER NUMBER,
    YEAR NUMBER
);
