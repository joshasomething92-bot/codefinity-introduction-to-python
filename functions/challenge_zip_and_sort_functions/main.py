# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]
# combined 3 lists into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))
# sorts the new tuple list in alphbetical order
sorted_products = sorted(combined_list)
# Need to loop through and print each tuple as its own
for product_name, price, quantity_sold in sorted_products:
    
    print(f"Product: {product_name}, Price: {price}, Quantity Sold: {quantity_sold} ")
    


