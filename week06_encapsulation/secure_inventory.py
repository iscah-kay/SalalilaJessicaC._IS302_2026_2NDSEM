class Product_jcs:
    def __init__(self_jcs, name_jcs, price_jcs, quantity_jcs):
        self_jcs.__name = name_jcs
        self_jcs.__price = price_jcs
        self_jcs.__quantity = quantity_jcs

    def get_product_info_jcs(self_jcs):
        print("Product:", self_jcs.__name)
        print("Price:", self_jcs.__price)
        print("Quantity:", self_jcs.__quantity)

    def update_quantity_jcs(self_jcs, new_quantity_jcs):
        if new_quantity_jcs >= 0:
            self_jcs.__quantity = new_quantity_jcs

    def update_price_jcs(self_jcs, new_price_jcs):
        if new_price_jcs > 0:
            self_jcs.__price = new_price_jcs

# Example usage
product_jcs = Product_jcs("Laptop", 45000, 10)
product_jcs.get_product_info_jcs()