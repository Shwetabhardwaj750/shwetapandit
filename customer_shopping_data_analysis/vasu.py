import numpy as np
import pandas as pd 
from io import StringIO
import os
file_path = os.path.join(os.path.dirname(__file__),"customer_shopping_data.csv")
df = pd.read_csv(file_path)
#first five rows
print(df.head(5))
#dataframe info
df.info()
#descreptive stat
print(df[['quantity','price']].describe())
#check for mssing values
print(df.isnull().sum())
#data cleaning

#handling missing values
df['quantity'] = df['quantity'].fillna(0)
# covert data types
df['invoice_date'] = pd.to_datetime(df['invoice_date'],errors="coerce",format="mixed")
df['quantity'] =df['quantity'].astype(int)
df['price'] = df['price'].astype(float)
#data exploration
df.columns = df.columns.str.strip()
# filter data
Kanyon_sales = df[df['shopping_mall'] == 'Kanyon']
print(Kanyon_sales)
 #sort data
top_10_price = df.sort_values(by = 'price',ascending = False).head(10)
print(top_10_price) 
print("top 10 products by price:",top_10_price)
#select specific columns
new_dataframe = df[['category','quantity','price']]
print(new_dataframe.head())
# sales revenue per category
total_sales_revenue_per_category = (df['quantity']*df['price']).groupby(df['category']).sum()
print(total_sales_revenue_per_category)
# avg
avg_quantity_mall = df.groupby('shopping_mall')['quantity'].mean()
print(avg_quantity_mall)
#most frequent customer gender
most_frequent_gender = df['gender'].mode(0)
print(f"most frequent gender is:{most_frequent_gender}")
# grouped analysis
df['revenue'] = df['quantity']*df['price']
grouped_revenue = df.groupby(['shopping_mall','category'])['revenue'].sum()
print(grouped_revenue)
#advanced analysis

#monthly sales trend 
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
df['ordermonth'] = df['invoice_date'].dt.to_period('M')
monthly_revenue = df.groupby('ordermonth')['revenue'].sum().reset_index()
print("total revenue per month:",monthly_revenue)
#highest total revenue
highest_month = monthly_revenue.loc[monthly_revenue.idxmax()]
print("highest month:",highest_month)
#shopping mall performance by category
mall_category_perf = df.groupby(['shopping_mall','category']).agg(
    total_revenue = ('revenue','sum'),
    total_quantity = ('quantity','sum'),
    transaction_count = ('invoice_no','count')
).reset_index()
print("mall_category_perf:",mall_category_perf)
#mall top category& total revenue
top_mall_categories = mall_category_perf.loc[
   mall_category_perf.groupby('shopping_mall')['total_revenue'].idxmax()
].rename(columns={'category':'top_category','total_revenue':'total_revenue'})
print("top_mall_categories:",top_mall_categories)

#customer gender spending habits

#avg revenue per order for each gender
avg_revenue_gender = df.groupby(['gender','invoice_no'])['revenue'].sum().reset_index()
#gender with highest revenue per order
gender_averages = avg_revenue_gender.groupby('gender')['revenue'].mean().reset_index()
#highest gender
highest_gender = gender_averages.loc[gender_averages['revenue'].idxmax()]
print(f"highest gender:{highest_gender['gender']} with {highest_gender['revenue']}")

#top N categories by revenue

#top  category entries with highest total revenue
top_categories_revenue = df.groupby('category')['revenue'].sum().reset_index()
#display top 5 categories and their total revenue
top_5_categories = top_categories_revenue.sort_values(by='revenue',ascending = False).head(5)
print("top_5_categories:",top_5_categories)









