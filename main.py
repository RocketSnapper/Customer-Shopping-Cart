from product import Product
from shoppingcart import ShoppingCart
from customer import Customer

product_one = Product('Blender', 49.99, 'Kitchen appliances')
product_two = Product('Baseball Bat', 65.98, 'Sports')

shoppingcart_one = ShoppingCart()
shoppingcart_one.add_product(['Necklace', 75.99, 'Jewelry'])
cart_price = shoppingcart_one.price_cart()
[print(cart_price)]
shoppingcart_one.empty_cart()

customer_one = Customer('John Mason')
customer_one.add_to_cart()