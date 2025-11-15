class ShoppingCart:
    def __init__(self, product_one, product_two):
        self.products = product_one + product_two

    def add_product(self, new_product):
        self.products += new_product
        print(self.products)
    
    def price_cart(self):
        cart_total = 0.00
        for product in self.products:
            if type(product) == float:
                cart_total += product
        return cart_total

    def empty_cart(self):
        self.products = []