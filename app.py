import tkinter as tk
from tkinter import font as tkfont
from loginPage import LoginPage
from customerPage import CustomerPage
from adminPage import AdminPage
from customer import Customer
from stockExchange import StockExchange
from userList import UserList

# App class, creates window for app, sets app settings, and creates frames for all app pages
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family='Helvetica', size=15, weight="bold")
        self.geometry("700x400")
        self.title("Stock Market Application")

        app_container = tk.Frame(self)
        app_container.pack(side="top", fill="both", expand=True)
        app_container.grid_rowconfigure(0, weight=1)
        app_container.grid_columnconfigure(0, weight=1)
        
        self.current_page = "LoginPage"

        self.user_list = UserList()
        self.stock_exchange = StockExchange()
        self.current_user = Customer("None", "None")

        self.frames = {}
        for FrameClass in (LoginPage, CustomerPage, AdminPage):
            page_name = FrameClass.__name__
            frame = FrameClass(parent=app_container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    # Pushes frame given to top of frame list, displaying the frame
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.current_page = page_name
        frame = self.frames[page_name]
        frame.tkraise()

    # Every second updates the price of stocks and displays updated price
    def updateStockPricesUI(self):
        if self.current_page == "CustomerPage":
            self.stock_exchange.updatePrices()
            self.show_frame("CustomerPage")
        self.after(2000, self.updateStockPricesUI)
    

if __name__ == "__main__":
    app = App()
    app.after(0, app.updateStockPricesUI)
    app.mainloop()
