from products import *


class Cart:
    def __init__(self):
        self.__products_list = []
        self.__cart_value = 0

    def addProduct(self, product):
        if isinstance(product, Product):
            if product not in self.__products_list:
                self.__products_list.append(product)
                self.calculateCart()

    def calculateCart(self):
        self.__cart_value = 0
        for element in self.__products_list:
            self.__cart_value += element.price

    def __str__(self):
        str_data = "\nCart info, products list:"
        for element in self.__products_list:
            str_data += '\n - ' + str(element.name) + " " + str(element.price)
        str_data += '\n Cart value: ' + str(self.__cart_value)
        return str_data
