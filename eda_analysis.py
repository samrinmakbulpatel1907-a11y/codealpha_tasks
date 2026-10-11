
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create project folder path
folder = Path(__file__).parent

# Create sample sales dataset
data = {
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Laptop", "Monitor",
        "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse",
        "Laptop", "Keyboard", "Monitor", "Mouse", "Laptop"
    ],
    "Category": [
        "Electronics", "Accessories", "Accessories",
        "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics", "Electronics",
        "Accessories", "Electronics", "Accessories",
        "Electronics", "Accessories", "Electronics"
    ],
    "Quantity": [2, 10, 5, 1, 3, 8, 4, 2, 2, 12, 1, 6, 2, 10, 1],
    "UnitPrice": [50000, 500, 1500, 50000, 12000, 500, 1500,
                  50000, 12000, 500, 50000, 1500, 12000, 500, 50000]
}

df = pd.DataFrame(data)

# Save the original dataset
df.to_csv(folder / "sales_data.csv", index=False)

print("===== SALES DATA ANALYSIS =====")

# 1. Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# 2. Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# 3. Check missing values and duplicates
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 4. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 5. Calculate sales
df["Sales"] = df["Quantity"] * df["UnitPrice"]

print("\nTotal Sales:")
print("Rs.", df["Sales"].sum())

print("\nSales by Product:")
product_sales = df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
)
print(product_sales)

print("\nSales by Category:")
category_sales = df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
)
print(category_sales)

print("\nBest-Selling Product by Quantity:")
print(df.groupby("Product")["Quantity"].sum().idxmax())

# 6. Save analysed dataset
df.to_csv(folder / "cleaned_sales_data.csv", index=False)

# 7. Chart: Sales by product
sns.set_theme(style="whitegrid")

product_sales.plot(kind="bar", figsize=(8, 5), title="Sales by Product")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig(folder / "sales_by_product.png")
plt.show()

# 8. Chart: Sales by category
category_sales.plot(kind="bar", figsize=(8, 5), title="Sales by Category")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig(folder / "sales_by_category.png")
plt.show()

# 9. Chart: Sales distribution
plt.figure(figsize=(8, 4))
sns.boxplot(x=df["Sales"])
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig(folder / "sales_boxplot.png")
plt.show()

print("\n===== EDA COMPLETED SUCCESSFULLY =====")
print("Dataset and charts saved in:", folder)
