# Stock class with name and price of stock
class Stock():
    def __init__(self, name, price):
        self.__name=name
        self.__price=price
    
    # Returns name of stock
    def getName(self):
        return self.__name
    
    # Returns price of stock
    def getPrice(self):
        return self.__price

    # Sets price of stock to value given
    def setPrice(self, price):
        self.__price = price
        return
    
    # Equality function for unit testing
    def __eq__(self, other):
        return self.getName() == other.getName() and self.getPrice() == other.getPrice()
