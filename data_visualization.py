
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Product": ["Notebook", "Pen", "Pencil", "Marker", "Eraser"],
    "Sales": [250, 100, 40, 120, 60]
}

df = pd.DataFrame(data)

print("DATA VISUALIZATION PROJECT")
print("\nSales Data:")
print(df)

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Sales"])
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_bar_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%"
)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("sales_pie_chart.png")
plt.show()

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df["Product"], df["Sales"], marker="o")
plt.title("Sales Trend by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_line_chart.png")
plt.show()

# Save data to CSV
df.to_csv("sales_data.csv", index=False)

print("\nOutput: Charts and CSV file created successfully!")
