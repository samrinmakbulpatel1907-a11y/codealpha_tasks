
# CodeAlpha - Exploratory Data Analysis (EDA)

## Project Overview
This project performs Exploratory Data Analysis on a sample sales dataset using Python.

## Objective
- Understand the dataset structure.
- Check missing values and duplicate records.
- Calculate total sales and product-wise sales.
- Compare sales across product categories.
- Visualize sales patterns using graphs.

## Tools and Libraries
- Python
- Pandas
- Matplotlib
- Seaborn

## Dataset
The project uses a sample sales dataset containing:
- Product
- Category
- Quantity
- UnitPrice

Sales are calculated using:

Sales = Quantity * UnitPrice

Note: This is a sample dataset created for learning and demonstration purposes.

## Analysis Performed
1. Displayed the first five records.
2. Checked dataset shape and data types.
3. Checked missing values and duplicate records.
4. Generated a statistical summary.
5. Calculated total sales.
6. Compared sales by product and category.
7. Created charts to visualize sales and distribution.

## Key Findings
- Total sales: Rs. 476,500
- Highest revenue product: Laptop
- Highest revenue category: Electronics
- Best-selling product by quantity: Mouse
- Missing values in the original dataset: 0
- Duplicate rows detected: 5

## Visualizations
- sales_by_product.png
- sales_by_category.png
- sales_boxplot.png

## How to Run
Install the required libraries:

pip install pandas matplotlib seaborn

Run the project:

python eda_analysis.py

## Conclusion
The analysis shows that laptops contribute the highest sales revenue in this sample dataset. Electronics is the leading category by revenue, while mice have the highest quantity sold.

This project demonstrates basic data inspection, statistical analysis, data quality checks, and visualization using Python.
