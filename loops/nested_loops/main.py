produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce] + [dairy]

for section in range(len(groceries)):
    for item in range(section):
        print(f"Item name: {groceries[0][0]}")
        print(f"Item name: {groceries[0][1]}")
        print(f"Item name: {groceries[1][0]}")
        print(f"Item name: {groceries[1][1]}")