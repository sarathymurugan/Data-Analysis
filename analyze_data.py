import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("sales_data.csv")

# Display the first few rows
print("Dataset Preview:")
print(data.head())

# Aggregate sales by product
product_sales = data.groupby("Product")["Sales"].sum()

# Plot the results
product_sales.plot(kind="bar", title="Total Sales by Product", color="skyblue")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_analysis.png")  # Save plot
plt.show()
