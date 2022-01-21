from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates
import datetime as st

root = Tk()
root.title('Currency Converter')
root.geometry("500x500")



#tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=3)

#Frames
currency_frame = Frame(my_notebook, width=480, height=480)
currency_frame.pack(fill="both", expand=1)

#add tabs
my_notebook.add(currency_frame, text='Currency')


#stuff
home = LabelFrame(currency_frame, text='Base currency')
home.pack(pady=20)

#home currency entry box
home_entry = Entry(home, font=('Helvetica', 24))
home_entry.pack(padx=10, pady=10)

#convert label
convert_label = LabelFrame(currency_frame, text='Convert to')
convert_label.pack(pady=20)

#convert entry
convert_entry = Entry(convert_label, font=('Helvetica', 24))
convert_entry.pack(padx=10, pady=10)

#currency codes
c = CurrencyRates()

#make a function
def d():
    equals_entry.delete(0, END)
    # base currency
    a = home_entry.get()
    a = a.upper()

    # Convert to
    b = convert_entry.get()
    b = b.upper()
    # Get rate
    e = c.get_rate(a, b)
    # convert price
    conversion = e
    #
    equals_entry.insert(0, conversion)

#button
button = Frame(convert_label)
button.pack(pady=20)

convert_button = Button(button, text='Convert', command=d)
convert_button.grid(row=0, column=0, padx=10)

#Equals
equals = LabelFrame(currency_frame, text='Equal to')
equals.pack(padx=10, pady=10)

equals_entry = Entry(equals, font=("Helvetica", 24), bd=0, bg="systembuttonface")
equals_entry.pack(pady=10, padx=10)




root.mainloop()


