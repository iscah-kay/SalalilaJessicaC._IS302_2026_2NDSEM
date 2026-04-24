product_jcs = input("Enter product name: ")
price_jcs = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_jcs + "," + price_jcs + "\n")

print("Product saved successfully")