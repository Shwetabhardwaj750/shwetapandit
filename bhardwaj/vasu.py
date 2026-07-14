import numpy as np
import pandas as pd 
from io import StringIO
import os
file_path = os.path.join(os.path.dirname(__file__),"customer_shopping_data.csv")
df = pd.read_csv(file_path)
print(df.head(5))
df.info()
print(df[['quantity','price']].describe())
print(df.isnull().sum())
#data cleaning
df['quantity'] = df['qunatity'].fillna(0)
df['invoice_date'] = pd.to_datetime(df['invioce_date'])
df['quantity'] = df['quantity'].astype(int)
df['price'] = df['price'].astype(float)
#data exploration 
Kanyon_sales = df[df['shopping mall']] == 'Kanyon'
print(Kanyon_sales)
top_10_price = df.sort_values(by = 'price',ascending = False.head(10))
print(top_10_price) 
print("top 10 products by price:",top_10_price)
new_dataframe = df[['category','quantity','price']]
print(new_dataframe.head())
total_sales_revenue_per_category = (df['quantity']*df['price']).groupby(df['category']).sum()
print(total_sales_revenue_per_category)
avg_quantity_mall = df.groupby('shopping_mall')['quantity'].mean()
print(avg_quantity_mall)
most_frequent_gender = df['gender'].mode[0]
print(f"most frequent gender is:{most_frequent_gender}")
df['revenue'] = df['quantity']*df['price']
grouped_revenue = df.groupby(['shopping_mall','category'])['revenue'].sum()
print(grouped_revenue)
#advanced analysis
#monthly sales trend 
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
df(['ordermonth']) == df['invoice_date'].dt.to_period('M')
monthly_revenue = df.groupby('ordermonth')['revenue'].sum().reset_index()
print("total revenue per month:",monthly_revenue)
highest_month = monthly_revenue.loc[monthly_revenue.idmax()]
#shopping mall performance




