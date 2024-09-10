from user import User
from portfolio import Portfolio

# Customer inherits from user, also contains a portfolio of stocks
class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.__portfolio = Portfolio()
    
    # Returns customer's portfolio
    def getPortfolio(self):
        return self.__portfolio



