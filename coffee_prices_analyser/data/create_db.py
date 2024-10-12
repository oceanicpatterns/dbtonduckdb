import duckdb

# Connect to or create a new DuckDB database inside your project folder
conn = duckdb.connect('coffee_prices.duckdb')

# Step 1: Create the 'coffee_prices' table (if it doesn't exist)
conn.execute('''
    CREATE TABLE IF NOT EXISTS coffee_prices (
        date DATE,
        value FLOAT
    );
''')

# Step 2: Import the CSV data into the 'coffee_prices' table
conn.execute('''
    INSERT INTO coffee_prices
    SELECT 
        CASE 
            WHEN CAST(date AS VARCHAR) LIKE '____-__-__' THEN CAST(date AS DATE)  -- YYYY-MM-DD format
            ELSE strptime(CAST(date AS VARCHAR), '%d.%m.%Y')::DATE  -- DD.MM.YYYY format
        END AS date,
        value 
    FROM read_csv_auto('coffee-prices-historical-data.csv',
        delim=',', 
        quote='"', 
        escape='"',
        header=True,
        types={'date': 'VARCHAR', 'value': 'FLOAT'},
        ignore_errors=True 
    );
''')

print("CSV data imported successfully into the 'coffee_prices' table!")

