-- models/staging/stg_coffee_prices.sql

WITH cleaned_data AS (
    SELECT
        CAST(date AS DATE) AS date,  -- Ensure dates are properly formatted
        value
    FROM {{ source('raw', 'coffee_prices') }}  -- Raw data table
    WHERE date IS NOT NULL  -- Clean any rows with missing dates
)

SELECT
    date,
    value
FROM cleaned_data;
