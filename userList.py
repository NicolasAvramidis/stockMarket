from customer import Customer
from admin import Admin

#List of users of app
class UserList():
    def __init__(self):
        self.__users = [
            Customer("navramid", "abc123"),
            Customer("12345", "54321"),
            Customer("testuser", "testpass"),
            Admin("admin", "admin")
        ] 
    
    # Returns username if customer added succesfully, None otherwise
    def addCustomer(self, username, password):
        if len(username) == 0 or len(password) == 0: return None
        for user in self.__users:
            if user.getUsername() == username:
                return None
        self.__users.append(Customer(username, password))
        return username

    # Returns username if customer removed succesfully, None otherwise   
    def removeCustomer(self, username):
        for user in self.__users:
            if user.getUsername() == username and isinstance(user, Customer):
                self.__users.remove(user)
                return username
        return None

    # Returns user if succesfully validated, None otherwise
    def validateLogin(self, username, password):
        for user in self.__users:
            if user.getUsername() == username and user.getPassword() == password:
                return user
        return None
