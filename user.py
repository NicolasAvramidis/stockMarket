# Base level user class
class User():
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    # Returns user's username
    def getUsername(self):
        return self.__username

    # Returns user's password
    def getPassword(self):
        return self.__password

    # Equality function for unit testing
    def __eq__(self, other):
        return self.getUsername() == other.getUsername() and self.getPassword() == other.getPassword()
