from product import Product
from shoppingcart import ShoppingCart

product_one = Product('Blender', 49.99, 'Kitchen appliances')
product_one.print_product()

product_two = Product('Baseball Bat', 65.98, 'Sports')

product_three = Product('Tent', 103.67, 'Outdoors')


shoppingcart_one = ShoppingCart([product_one.name, product_one.price, product_one.category], {product_two})
shoppingcart_one.price_cart(product_one.price, product_two.price, product_three.price)
shoppingcart_one.add_product()

