-- models/marts/refined_coffee_price_analysis.sql

WITH yearly_avg_prices AS (
    SELECT
        YEAR(date) AS year,
        AVG(price_per_kg) AS avg_price_per_kg
    FROM {{ ref('stg_coffee_prices') }}  -- Use the staging model
    GROUP BY year
)

SELECT
    year,
    avg_price_per_kg
FROM yearly_avg_prices
ORDER BY year;
