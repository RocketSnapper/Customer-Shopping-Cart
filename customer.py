from shoppingcart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.products = ShoppingCart()

    def add_to_cart(self):
        self.products.add_product(['Slinky', 9.99, 'Toys'])
        