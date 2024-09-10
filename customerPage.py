import tkinter as tk
from functools import partial
from user import User
from stockExchange import StockExchange
from customer import Customer

# Customer page: displays username, gives ability to add balance, shows all stocks and allows buying/selling, displays profits
class CustomerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Label that displays current and their balance 
        self.nameLabel = tk.Label(self, text=f"{self.controller.current_user.getUsername()} Balance:", font=controller.title_font)
        self.balanceLabel = tk.Label(self, text=f"${self.controller.current_user.getPortfolio().getBalance():.2f}", font=controller.title_font, width=10)
        self.nameLabel.grid(row=0, column=0, padx=10, pady=10)
        self.balanceLabel.grid(row=0, column=1, padx = 10, pady=10)

        # Add balance form and button
        self.addBalanceEntry = tk.Entry(self, bd = 5)
        self.addBalanceButton = tk.Button(self, text="Add Balance", command=self.addBalanceAction)
        self.addBalanceEntry.grid(row=0, column=2, padx = 10, pady=10)
        self.addBalanceButton.grid(row=0, column=3, padx = 10, pady=10)

        # Loop that created grid for every stock in exchange, with price, buy/sell buttons, and number owned by user
        self.stocks_ui_dict = {}
        for i, stock in enumerate(self.controller.stock_exchange.getStockList()):
            temp_list = []
            temp_list.append(tk.Label(self, text=f"{stock.getName()} : {stock.getPrice()}", width=30))
            temp_list.append(tk.Button(self, text="Sell", command=partial(self.sellButton, stock)))
            temp_list.append(tk.Label(self, text=f"{self.controller.current_user.getPortfolio().getQuantity(stock.getName())}"))
            temp_list.append(tk.Button(self, text="Buy", command=partial(self.buyButton, stock)))

            temp_list[0].grid(row=i+1, column=0, sticky="w", padx = 10, pady = 5)
            temp_list[1].grid(row=i+1, column=1, padx = 10, pady = 5)
            temp_list[2].grid(row=i+1, column=2, padx = 10, pady = 5)
            temp_list[3].grid(row=i+1, column=3, padx = 10, pady = 5)

            self.stocks_ui_dict[stock.getName()] = temp_list

        # Label that displays user's profits
        self.netGainTitle = tk.Label(self, text=f"Net Gain/Loss:", font=controller.title_font)
        self.netGainTitle.grid(row=len(self.stocks_ui_dict)+2, column=0, padx = 10, pady=10)
        self.netGain = tk.Label(self, text=f"${self.controller.current_user.getPortfolio().getNetGain(self.controller.stock_exchange):.2f}", font=controller.title_font)
        self.netGain.grid(row=len(self.stocks_ui_dict)+2, column=1, padx = 10, pady=10)

        # Log out button
        self.logOut = tk.Button(self, text=f"Log Out", command=self.logOutButton)
        self.logOut.grid(row=len(self.stocks_ui_dict)+2, column=3, padx = 10, pady=10)

    # Adds balance on success, clears form and refreshes page
    def addBalanceAction(self):
        try:
            self.controller.current_user.getPortfolio().addBalance(float(self.addBalanceEntry.get()))
            self.addBalanceEntry.delete(0, "end")
            self.controller.show_frame("CustomerPage")
        except:
            self.addBalanceEntry.delete(0, "end")
            self.controller.show_frame("CustomerPage")

    # Sells stock and refreshes page
    def sellButton(self, stock):
        self.controller.current_user.getPortfolio().sellStock(self.controller.stock_exchange, stock.getName())
        self.controller.show_frame("CustomerPage")

    # Buys stock and refreshes page
    def buyButton(self, stock):
        self.controller.current_user.getPortfolio().buyStock(self.controller.stock_exchange, stock.getName())
        self.controller.show_frame("CustomerPage")

    # Logs out of current customer and switches frame to login page
    def logOutButton(self):
        self.controller.current_user = Customer("None", "None")
        self.controller.show_frame("LoginPage")

    # Function for updating gui widgets when page is refreshed
    def tkraise(self):
        self.nameLabel.configure(text=f"{self.controller.current_user.getUsername()} Balance:")
        self.balanceLabel.configure(text=f"${round(self.controller.current_user.getPortfolio().getBalance(), 2):.2f}")
        
        for stock_ui_elem in self.stocks_ui_dict:
            self.stocks_ui_dict.get(stock_ui_elem)[0].configure(text=f"{stock_ui_elem} : {round(self.controller.stock_exchange.getStock(stock_ui_elem).getPrice(), 2)}")
            self.stocks_ui_dict.get(stock_ui_elem)[2].configure(text=f"{self.controller.current_user.getPortfolio().getQuantity(stock_ui_elem)}")

        self.netGain.configure(text=f"${(round(self.controller.current_user.getPortfolio().getNetGain(self.controller.stock_exchange), 2) + 0):.2f}")
        if round(self.controller.current_user.getPortfolio().getNetGain(self.controller.stock_exchange), 2) >= 0:
            self.netGain.configure(fg="Green")
        else:
            self.netGain.configure(fg="Red")
            
        super().tkraise()
