from order import *


def run():
    product1 = Product("Candy", 12.00)
    print(product1)
    product2 = Product("Clothes", 300.00)
    print(product2)
    product3 = Product("Book", 200.00)
    print(product3)
    
    listOfProducts=[product2]
    order1 = Order(listOfProducts)
    order1.add_product(product1)
    order1.add_product(product3)
    print (order1.calculate_total())
    print(product1+product2)
    


if __name__ == "__main__":
    run()
