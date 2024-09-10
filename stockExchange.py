import random
from stock import Stock

# Stock exchange containing list of currently available stocks
class StockExchange():
    def __init__(self):
        self.__stocks = [
            Stock("Apple", 100.00),
            Stock("Google", 80.13),
            Stock("Amazon", 110.67),
            Stock("Disney", 78.04),
            Stock("Meta", 97.34),
            Stock("IBM", 67.65),
            Stock("Tesla", 114.43)
        ]
    
    # Returns Stock list
    def getStockList(self):
        return self.__stocks

    # Stock name is given, returns stock if it exists, None otherwise
    def getStock(self, stock_name):
        for stock in self.__stocks:
            if stock.getName() == stock_name:
                return stock
        return None

    # Prices of all stocks in exchange are updated, returns nothing
    def updatePrices(self):
        for stock in self.__stocks:
            new_price = stock.getPrice() + round(stock.getPrice()*random.uniform(-0.1, 0.1), 2)
            if new_price <= 0:
                new_price = 0
            stock.setPrice(new_price)
        return
