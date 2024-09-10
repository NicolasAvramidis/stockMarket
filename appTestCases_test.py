import unittest
from portfolio import Portfolio
from stockExchange import StockExchange
from stock import Stock
from user import User
from admin import Admin
from customer import Customer
from userList import UserList

class portfolio_test(unittest.TestCase):
    def testEmptyStockList(self):
        portfolio1 = Portfolio()
        self.assertEqual(portfolio1.getStocksDict(), {})
    
    def testEmptyBalance(self):
        portfolio1 = Portfolio()
        self.assertEqual(portfolio1.getBalance(), 0.00)
    
    def testBalance1(self):
        portfolio1 = Portfolio()
        portfolio1.addBalance(103.11)
        self.assertEqual(portfolio1.getBalance(), 103.11)
    
    def testBalance2(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)
        portfolio1.buyStock(exchange1, "Apple")
        self.assertEqual(portfolio1.getBalance(), 900.00)

    def testBalance3(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)
        portfolio1.buyStock(exchange1, "Apple")
        portfolio1.sellStock(exchange1, "Apple")
        self.assertEqual(portfolio1.getBalance(), 1000.00)
    
    def testTotalMoney(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)
        portfolio1.buyStock(exchange1, "Apple")
        self.assertEqual(portfolio1.getTotalMoneyAdded(), 1000.00)
    
    def testBuyStock(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)       
        self.assertEqual(portfolio1.buyStock(exchange1, "Apple"), "Apple")

    def testBuyingNonExistantStock(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)       
        self.assertEqual(portfolio1.buyStock(exchange1, "Asus"), None)

    def testSellStock(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)
        portfolio1.buyStock(exchange1, "Apple")
        self.assertEqual(portfolio1.sellStock(exchange1, "Apple"), "Apple")

    def testSellingUnownedStock(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)
        portfolio1.buyStock(exchange1, "Apple")
        portfolio1.sellStock(exchange1, "Apple")
        self.assertEqual(portfolio1.sellStock(exchange1, "Apple"), None)

    def testSellingNonExistantStock(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()      
        self.assertEqual(portfolio1.sellStock(exchange1, "Asus"), None)
    
    def testAddBalance(self):
        portfolio1 = Portfolio()
        self.assertEqual(portfolio1.addBalance(150.23), 150.23)

    def testQuantity1(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000)
        portfolio1.buyStock(exchange1, "Apple")
        portfolio1.buyStock(exchange1, "Apple")
        self.assertEqual(portfolio1.getQuantity("Apple"), 2)

    def testQuantity2(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(10.00)
        portfolio1.buyStock(exchange1, "Apple")
        portfolio1.buyStock(exchange1, "Apple")
        self.assertEqual(portfolio1.getQuantity("Apple"), 0)

    def testNetGain(self):
        exchange1 = StockExchange()
        portfolio1 = Portfolio()
        portfolio1.addBalance(1000.00)
        portfolio1.buyStock(exchange1, "Apple")
        portfolio1.buyStock(exchange1, "Tesla")
        portfolio1.sellStock(exchange1, "Apple")
        self.assertEqual(portfolio1.getNetGain(exchange1), 0)


class stockExchange_test(unittest.TestCase):
    def testCorrectStockList(self):
        stockExchange1 = StockExchange()
        self.assertEqual(stockExchange1.getStockList(), 
        [   Stock("Apple", 100.00),
            Stock("Google", 80.13),
            Stock("Amazon", 110.67),
            Stock("Disney", 78.04),
            Stock("Meta", 97.34),
            Stock("IBM", 67.65),
            Stock("Tesla", 114.43)])
    
    def testGetStock1(self):
        stockExchange1 = StockExchange()
        self.assertEqual(stockExchange1.getStock("Apple"), Stock("Apple", 100.00))
    
    def testGetStock2(self):
        stockExchange1 = StockExchange()
        self.assertNotEqual(stockExchange1.getStock("Google"), Stock("Google", 333.33))


class stock_test(unittest.TestCase):
    def testCorrectStockName(self):
        stock1 = Stock("Apple", 100.0)
        self.assertEqual(stock1.getName(), "Apple")

    def testIncorrectStockName(self):
        stock1 = Stock("Apple", 100.0)
        self.assertNotEqual(stock1.getName(), "Google")

    def testCorrectStockPrice(self):
        stock1 = Stock("Google", 123.45)
        self.assertEqual(stock1.getPrice(), 123.45)
    
    def testStockPrice1(self):
        stock1 = Stock("Google", 123.45)
        stock1.setPrice(100.99)
        self.assertEqual(stock1.getPrice(), 100.99)
    
    def testStockPrice2(self):
        stock1 = Stock("Google", 123.45)
        stock1.setPrice(100.99)
        stock1.setPrice(44.44)
        self.assertEqual(stock1.getPrice(), 44.44)
    
    def testStockPrice3(self):
        stock1 = Stock("Google", 123.45)
        stock1.setPrice(-10)
        self.assertEqual(stock1.getPrice(), -10)
    
    def testStockEquality(self):
        stock1 = Stock("Google", 123.45)
        stock2 = Stock("Google", 123.45)
        self.assertEqual(stock1, stock2)
    
    def testStockEquality(self):
        stock1 = Stock("Google", 123.45)
        stock2 = Stock("Apple", 123.45)
        self.assertNotEqual(stock1, stock2)


class user_test(unittest.TestCase):
    def testGetUsername1(self):
        user1 = User("username", "password")
        self.assertEqual(user1.getUsername(), "username")

    def testGetUsername2(self):
        user1 = User("12345", "12345")
        self.assertEqual(user1.getUsername(), "12345")

    def testGetPassword1(self):
        user1 = User("username", "password")
        self.assertEqual(user1.getPassword(), "password")

    def testGetPassword2(self):
        user1 = User("12345", "12345")
        self.assertEqual(user1.getPassword(), "12345")

    def testSameUser(self):
        user1 = User("username", "password")
        user2 = User("username", "password")
        self.assertEqual(user1, user2)
    
    def testDifferentUser1(self):
        user1 = User("username", "password")
        user2 = User("abc", "password")
        self.assertNotEqual(user1, user2)

    def testDifferentUser2(self):
        user1 = User("username", "password")
        user2 = User("abc", "123")
        self.assertNotEqual(user1, user2)


class customer_test(unittest.TestCase):
    def testGetPortfolio(self):
        customer1 = Customer("username", "password")
        customer1.getPortfolio().addBalance(100.00)
        self.assertEqual(customer1.getPortfolio().getBalance(), 100.00)


class userList_test(unittest.TestCase):
    def testAddCustomer(self):
        userList1 = UserList()
        self.assertEqual(userList1.addCustomer("username", "password"), "username")

    def testAddExistingCustomer1(self):
        userList1 = UserList()
        userList1.addCustomer("username", "password")
        self.assertEqual(userList1.addCustomer("username", "password"), None)

    def testAddExistingCustomer2(self):
        userList1 = UserList()
        userList1.addCustomer("username", "password")
        self.assertEqual(userList1.addCustomer("username", "different"), None)

    def testAddBadCustomer1(self):
        userList1 = UserList()
        self.assertEqual(userList1.addCustomer("", ""), None)

    def testAddBadCustomer2(self):
        userList1 = UserList()
        self.assertEqual(userList1.addCustomer("username", ""), None)

    def testAddBadCustomer3(self):
        userList1 = UserList()
        self.assertEqual(userList1.addCustomer("", "password"), None)

    def testRemoveCustomer(self):
        userList1 = UserList()
        userList1.addCustomer("username", "password")
        self.assertEqual(userList1.removeCustomer("username"), "username")
    
    def testRemoveNonExistingCustomer(self):
        userList1 = UserList()
        self.assertEqual(userList1.removeCustomer("username"), None)
    
    def testRemoveAdmin(self):
        userList1 = UserList()
        self.assertEqual(userList1.removeCustomer("admin"), None)

    def testValidateCustomer1(self):
        userList1 = UserList()
        userList1.addCustomer("username", "password")
        self.assertEqual(userList1.validateLogin("username", "password"), Customer("username", "password"))

    def testValidateCustomer2(self):
        userList1 = UserList()
        userList1.addCustomer("username", "password")
        self.assertEqual(userList1.validateLogin("username", "different"), None)

    def testValidateCustomer3(self):
        userList1 = UserList()
        userList1.addCustomer("username", "password")
        self.assertEqual(userList1.validateLogin("different", "password"), None)

    def testValidateAdmin1(self):
        userList1 = UserList()
        self.assertEqual(userList1.validateLogin("admin", "admin"), Admin("admin", "admin"))

    def testValidateAdmin2(self):
        userList1 = UserList()
        self.assertEqual(userList1.validateLogin("admin", "different"), None)

    def testValidateAdmin3(self):
        userList1 = UserList()
        self.assertEqual(userList1.validateLogin("different", "admin"), None)