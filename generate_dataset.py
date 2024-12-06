import pandas as pd
import random
from datetime import datetime, timedelta

# Define random data generation
def random_date(start, end):
    """Generate a random date between two dates."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_product():
    """Random product names."""
    return random.choice(["Product A", "Product B", "Product C", "Product D", "Product E"])

def random_region():
    """Random regions."""
    return random.choice(["North", "South", "East", "West"])

# Generate dataset
rows = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

for _ in range(100):  # 100 rows
    date = random_date(start_date, end_date).strftime("%Y-%m-%d")
    product = random_product()
    region = random_region()
    sales = random.randint(50, 500)
    revenue = round(sales * random.uniform(10, 50), 2)
    cost = round(revenue * random.uniform(0.5, 0.9), 2)
    profit = round(revenue - cost, 2)
    satisfaction = random.randint(1, 10)
    discount = random.uniform(5, 30)  # Percentage
    units_sold = random.randint(10, 100)
    
    rows.append([date, product, region, sales, revenue, profit, cost, satisfaction, discount, units_sold])

# Create DataFrame
columns = ["Date", "Product", "Region", "Sales", "Revenue", "Profit", "Cost", 
           "Customer_Satisfaction", "Discount_Percentage", "Units_Sold"]
df = pd.DataFrame(rows, columns=columns)

# Save to CSV
df.to_csv("sales_data.csv", index=False)

print("Dataset 'sales_data.csv' created with 100 rows and 10 columns.")
