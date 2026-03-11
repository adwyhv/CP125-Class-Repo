# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    f = open("data/order.csv","r")


    
result = calculate_order_total("data/products.csv", "data/order.csv", "data/total.csv")
print(f"Grand total: ${result:.2f}")
