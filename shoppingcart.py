class ShoppingCart:
    def __init__(self, product_one, product_two):
        self.products = product_one + product_two

    def add_product(self):
        print(self.products)
    
    def price_cart(self,product_a, product_b, product_c):
        cart_total = product_a + product_b +product_c
        print(cart_total)
        return cart_total

    def empty_cart():
        print()