import matplotlib.pyplot as plt
import duckdb

# Connect to or create a new DuckDB database inside your project folder
conn = duckdb.connect('coffee_prices.duckdb')

# Fetch the data
results = conn.execute('''
    SELECT 
        strftime(date, '%Y') AS year, 
        AVG(value) AS avg_price
    FROM coffee_prices
    GROUP BY year
    ORDER BY year
''').fetchdf()

# Plot the results
plt.plot(results['year'], results['avg_price'])
plt.xlabel('Year')
plt.ylabel('Average Price (GBP)')
plt.title('Average Coffee Price per Year in the UK')
plt.show()
