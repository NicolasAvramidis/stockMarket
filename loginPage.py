import tkinter as tk
from userList import UserList
from customer import Customer
from admin import Admin

# Login page with username and password forms, as well as button to login
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title
        login_label = tk.Label(self, text="Login Page", font=self.controller.title_font)
        login_label.pack(side="top", fill="x", pady=10)

        # Username form
        self.username = tk.Entry(self, bd = 5)
        self.username.pack(padx = 10, pady = 10)

        # Password form
        self.password = tk.Entry(self, bd = 5, show="*")
        self.password.pack(padx = 10, pady = 10)

        # Login Button
        login_button = tk.Button(self, text="Log In", command=self.loginButtonPress)
        login_button.pack()

        # Label displaying preset login info for new users
        login_help_label = tk.Label(self, text="For customer try 'testuser, testpass' or '12345, 54321' - for Admin try 'admin, admin'")
        login_help_label.pack(side="bottom", fill="x", pady=10)

    # On sucess, switches frames to user page, on failure clears username and password forms 
    def loginButtonPress(self):
        if self.controller.user_list.validateLogin(self.username.get(), self.password.get()):
            self.controller.current_user = self.controller.user_list.validateLogin(self.username.get(), self.password.get())
            if isinstance(self.controller.current_user, Customer):
                self.controller.show_frame("CustomerPage")
            elif isinstance(self.controller.current_user, Admin):
                self.controller.show_frame("AdminPage")

        self.username.delete(0, "end")
        self.password.delete(0, "end")
        return
