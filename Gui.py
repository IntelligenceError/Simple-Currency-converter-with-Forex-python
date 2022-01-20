from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title('Currency Converter')
root.geometry("500x500")

#tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

#Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

#add tabs
my_notebook.add(currency_frame, text='Currency')
my_notebook.add(conversion_frame, text='Convert')

#disable tabs
my_notebook.tab(1, state='disable')

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WARNING", "You didn't fill out all the fill")
    else:
        #disable entry boxes
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        #enable tabs
        my_notebook.tab(1, state='normal')
        #change tab field
        amount_label.config(text=f'Amount of {home_entry.get()} to convert to {conversion_entry.get()}')
        convert_label.config(text=f'Equals This Many {conversion_entry.get()}')
        convert_button.config(text=f'Convert from {home_entry.get()}')


def unlock():
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    #disable tabs
    my_notebook.tab(1, state="disabled")


#stuff
home = LabelFrame(currency_frame, text='Base currency')
home.pack(pady=20)

#home currency entry box
home_entry = Entry(home, font=('Helvetica', 24))
home_entry.pack(padx=10, pady=10)

#conversion currency frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

#conversion label
conversion_label = Label(conversion, text="Currency to convert to")
conversion_label.pack(pady=10)

#convert to entry
conversion_entry = Entry(conversion, font=('Helvetica', 24))
conversion_entry.pack(padx=10, pady=10)

#rate label
rate_label = Label(conversion, text="Current conversion rate")
rate_label.pack(pady=10)

#rate entry
rate_entry = Entry(conversion, font=('Helvetica', 24))
rate_entry.pack(padx=10, pady=10)

#button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

#create button
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

##################
def Convert():
    #Clear convert entry box
    convert_entry.delete(0, END)
    #Convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    #Update entry box
    convert_entry.insert(0, conversion)
    #round off
    conversion = round(conversion, 2)
    #comma
    conversion = '{:,}'.format(conversion)
    #Update entry box
    convert_entry.insert(0, f'${conversion}')


def clear():
    amount_entry.delete(0, END)
    convert_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text="Amount to convert")
amount_label.pack(pady=10)
# Entry box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(padx=10, pady=10)
#convert button
convert_button = Button(amount_label, text="Convert", command=Convert)
convert_button.pack(pady=20)

#Equals
convert_label = LabelFrame(conversion_frame, text="Converted Currency")
convert_label.pack(pady=10)

convert_entry = Entry(convert_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
convert_entry.pack(pady=10, padx=10)

#clear
clear_button = Button(conversion_frame, text="Clear",command=clear)
clear_button.pack(pady=10)

#create space
space = Label(conversion_frame, text="", width=68)##
space.pack()



root.mainloop()


