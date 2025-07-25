from tkinter import *
from tkinter import messagebox
from random import sample
import pyperclip

SAVE_LOCATION = "data.txt"
# noinspection DuplicatedCode
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = [letter for letter in LETTERS] + [symbol for symbol in SYMBOLS] + [number for number in NUMBERS]
    password = ''.join(sample(password_list, 10))

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror('Not enough data!','Some fields are missing')
        return
    is_ok = messagebox.askokcancel(title="Saving Data", message=f'The current data to be saved are:\nEmail: {website_entry.get()}\nPassword: {password_entry.get()}')

    if is_ok:
        with open(SAVE_LOCATION, 'a+') as file:
            file.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')
    else:
        return


    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo(title="Success", message="Data saved successfully")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_text = Label(text='Website:')
website_text.grid(row=2,column=0)
website_entry = Entry(width=35)
website_entry.grid(row=2,column=1,sticky='we',columnspan=2)

email_text = Label(text='Email/Username:')
email_text.grid(row=3, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=3,column=1,sticky='we',columnspan=2)

password_text = Label(text='Password:')
password_text.grid(row=4,column=0)
password_entry = Entry(width=33)
password_entry.grid(row=4,column=1, sticky='w')
password_generate = Button(text='Generate Password', command=generate_password)
password_generate.grid(row=4,column=2)

add_button = Button(text='Add',width=36,command=save)
add_button.grid(row=5,column=1,columnspan=2,sticky='we')


window.mainloop()