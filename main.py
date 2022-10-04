from cart import *

phone1 = Phone('Phone X', 5000, 'red')
tv1 = TV('Samsung', 10000, 65)
cart = Cart()
cart.addProduct(phone1)
cart.addProduct(tv1)
print(cart)
