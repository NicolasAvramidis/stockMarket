from user import User

# Admin inherits from user, can access UI pages a customer cannot. Checked with isinstance(user, Admin)
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    

