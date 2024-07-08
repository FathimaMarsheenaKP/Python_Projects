from openpyxl import workbook, load_workbook
import tkinter as tk
from tkinter import Label, Entry, Button
################################

class DataEntryForm(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("Data Entry Form")
        self.geometry("500x400")

        self.item_label = Label(self, text = 'Item')
        self.item_entry = Entry(self)

        self.quantity_label = Label(self, text = 'Quantity')
        self.quantity_entry = Entry(self)

        self.price_label = Label(self, text = 'Price')
        self.price = Entry(self)





app = DataEntryForm()
app.mainloop()



