# Product Class definition

class Product:
    # class variable
    product_counter = 0

    def __init__(self, name, price):
        Product.add_product()
        self._id_product = self.product_counter
        self._name = name
        self._price = float(price)

    # Attributes
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    # Class Method
    @classmethod
    def add_product(cls):
        cls.product_counter += 1

    # Methods
    def __str__(self):
        return f"Id Product: {self._id_product}, Name: {self.name}, Price: {self._price}"
    
    def __add__(self,product1):  # ---> objec1.__add__(object2)
        return (self.price + product1.price)
        


# Order Class definition
class Order:
    # Class Variable
    order_counter = 0

    def __init__(self, product_list):
        Order.add_order()
        self._id_order = self.order_counter
        self._product_list = product_list

    # Attributes
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, product):
        self._product_list = list(product)

    # Class Method
    @classmethod
    def add_order(cls):
        cls.order_counter += 1

    # Methods
    def __str__(self):
        return f"Id Order: {self._id_order}, List of products : {self._product_list}"

    def add_product(self, product):
        self._product_list.append(product)

    def calculate_total(self):
        total = 0
        for item in self._product_list:
            total = item.price + total
        return total

