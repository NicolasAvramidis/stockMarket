import tkinter as tk
from userList import UserList

# Admin page: Allows admins to add and remove users
class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Admin page title label
        self.admin_page_label = tk.Label(self, text="Admin Controls", font=self.controller.title_font)
        self.admin_page_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Form for entering customer username
        self.remove_customer_form = tk.Entry(self, bd = 5)
        self.remove_customer_form.grid(row=1, column=0, padx = 10, pady=10)
        
        # Button for removing customer
        self.remove_customer_button = tk.Button(self, text="Remove Customer", command=self.removeCustomerButton)
        self.remove_customer_button.grid(row=1, column=1, padx = 10, pady=10)

        # Remove customer label
        self.remove_customer_label = tk.Label(self, text="")
        self.remove_customer_label.grid(row=1, column=2, padx = 10, pady=10)

        # Form for entering customer username and password
        self.add_customer_user_form = tk.Entry(self, bd = 5)
        self.add_customer_pass_form = tk.Entry(self, bd = 5)
        self.add_customer_user_form.grid(row=2, column=0, padx = 10, pady=10)
        self.add_customer_pass_form.grid(row=2, column=1, padx = 10, pady=10)

        # Button for adding customer
        self.add_customer_button = tk.Button(self, text="Add Customer", command=self.addCustomerButton)
        self.add_customer_button.grid(row=2, column=2, padx = 10, pady=10)

        # Add Customer Label
        self.add_customer_label = tk.Label(self, text="")
        self.add_customer_label.grid(row=2, column=3, padx = 10, pady=10)

        # Log out button
        self.logOut = tk.Button(self, text=f"Log Out", command=self.logOutButton)
        self.logOut.grid(row=4, column=0, padx = 10, pady=10)

        return
    
    # Removes customer and clears form on succes, refreshes page
    def removeCustomerButton(self):
        user_name = self.controller.user_list.removeCustomer(self.remove_customer_form.get())
        if user_name:
            self.remove_customer_form.delete(0, "end")
            self.controller.show_frame("AdminPage")
            self.remove_customer_label.configure(text=f"Customer {user_name} Removed")
            return
        self.controller.show_frame("AdminPage")
    
    # Adds customer and clears forms on succes, refreshes page
    def addCustomerButton(self):
        user_name = self.controller.user_list.addCustomer(self.add_customer_user_form.get(), self.add_customer_pass_form.get())
        if user_name:
            self.add_customer_user_form.delete(0, "end")
            self.add_customer_pass_form.delete(0, "end")
            self.controller.show_frame("AdminPage")
            self.add_customer_label.configure(text=f"Customer {user_name} Added")
            return
        self.controller.show_frame("AdminPage")
    
    # Logs out of Admin and switches frame to login page
    def logOutButton(self):
        self.controller.show_frame("LoginPage")

    # Function for updating gui widgets when page is refreshed
    def tkraise(self):
        self.remove_customer_label.configure(text=f"")
        self.add_customer_label.configure(text=f"")   
        super().tkraise()