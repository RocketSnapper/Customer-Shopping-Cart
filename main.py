from product import Product
from shoppingcart import ShoppingCart

product_one = Product('Blender', 49.99, 'Kitchen appliances')
product_two = Product('Baseball Bat', 65.98, 'Sports')

shoppingcart_one = ShoppingCart([product_one.name, product_one.price, product_one.category], [product_two.name, product_two.price, product_two.category])
shoppingcart_one.add_product(['Necklace', 75.99, 'Jewelry'])
cart_price = shoppingcart_one.price_cart()
shoppingcart_one.empty_cart()

