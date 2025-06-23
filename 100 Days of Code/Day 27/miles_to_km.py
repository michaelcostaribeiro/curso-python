from tkinter import *

FONT = ('Arial', 12)

window = Tk()
window.minsize(width=300, height=125)
window.title('Mile to Km Converter')
window.config(padx=30, pady=30)

converted_km = 0

def is_number(inp):
    return True if type(inp) == int or type(inp) == float else False

def miles_to_km():
    miles = miles_entry.get()
    try:
        miles = float(miles)
        km_number.config(text=miles * 1.60934)
    except ValueError:
        km_number.config(text='numbers only!')


miles_entry = Entry()
miles_entry.grid(row=0, column=1)

miles_text = Label(text='Miles', font=FONT)
miles_text.grid(row=0,column=2)

is_equal_to = Label(text='is equal to:', font=FONT)
is_equal_to.grid(row=1,column=0)

km_number = Label(text=converted_km, font=FONT)
km_number.grid(row=1,column=1)

km_string = Label(text='Km', font=FONT)
km_string.grid(row=1,column=2)

calculate = Button(text='Calculate', font=FONT, command=miles_to_km)
calculate.grid(row=2,column=1)

window.mainloop()
