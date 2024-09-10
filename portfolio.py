# Portfolio containg dict of stocks owned and current cash balance, as well as total money added to account
class Portfolio():
    def __init__(self):
        self.__stocks = {}
        self.__balance = 0.0
        self.__totalMoneyAdded = 0.0
    
    # Returns dict of stocks owned
    def getStocksDict(self):
        return self.__stocks

    # Returns current balance
    def getBalance(self):
        return self.__balance
    
    # Returns total money added to account
    def getTotalMoneyAdded(self):
        return self.__totalMoneyAdded
    
    # Adds to balance if amount is greater balance, returns new balance
    def addBalance(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__totalMoneyAdded += amount
        return self.__balance

    # Returns number owned of particular stock, or 0 if stock name is not in dict
    def getQuantity(self, stock_name):
        return self.__stocks.get(stock_name, 0)

    # If stock exists and customer can afford stock, add one to stock dict, returns stock name on sucess and None on failure 
    def buyStock(self, exchange, stock_name):
        stock = exchange.getStock(stock_name)
        if not stock:
            return None
        
        if self.__balance >= stock.getPrice():
            if stock.getName() in self.__stocks:
                self.__stocks[stock.getName()] += 1
            else:
                self.__stocks[stock.getName()] = 1
            self.__balance -= stock.getPrice()
        else:
            return None
        
        return stock_name

    # If stock exists and customer owns stock, remove one from stock dict, returns stock name on sucess and None on failure
    def sellStock(self, exchange, stock_name):
        stock = exchange.getStock(stock_name)
        if not stock:
            return None
        
        if (stock.getName() in self.__stocks) and (self.__stocks[stock.getName()] > 0):
            self.__stocks[stock.getName()] -= 1
            self.__balance += stock.getPrice()
        else:
            return None
        
        return stock_name

    # Returns net profits of customer, value of stock owned and cash balance, minus total money added
    def getNetGain(self, exchange):
        stockValue = 0.0
        for stock_name in self.__stocks:
            stockValue += exchange.getStock(stock_name).getPrice() * self.__stocks.get(stock_name, 0)
        return (stockValue + self.__balance) - self.__totalMoneyAdded

    # Equality function for unit testing
    def __eq__(self, other):
        return self.getStocksList() == other.getStocksList() and self.getBalance() == other.getBalance() and self.getTotalMoneyAdded() == other.getTotalMoneyAdded()