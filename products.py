class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.name) + " " + str(self.price)


class Phone(Product):
    def __init__(self, name, price, color):
        Product.__init__(self, name, price)
        self.color = color

    def __str__(self):
        return super().__str__() + " " + str(self.color)


#phone1 = Phone('Iphone', 5000, 'red')
# print(phone1)


class TV(Product):
    def __init__(self, name, price, screen_size):
        super().__init__(name, price)
        self.screen_size = screen_size

    def __str__(self):
        return super().__str__() + " " + str(self.screen_size)


#tv1 = TV('Samsung', 4500, 65)
# print(tv1)
