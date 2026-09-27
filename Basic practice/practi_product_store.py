class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count = Product.count + 1

    def get_info(self):  # instance method
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total objects = {cls.count}")

    @staticmethod
    def calc_discount(price, percentage):
        print(f"Discount price = {price - (price * percentage / 100)}")


p1 = Product("Phone", 80000)
p2 = Product("Laptop", 20000)

Product.calc_discount(100000, 12) 