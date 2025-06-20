from tkinter import *
from tkinter import messagebox
from random import sample
import pyperclip
import json

SAVE_LOCATION = "data.json"
# noinspection DuplicatedCode
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ---------------------------------- SEARCH ------------------------------------- #
def find_password():
    try:
        with open(SAVE_LOCATION, 'r') as file:
            data = json.load(file)
            if website_entry.get() in data:
                site = data[website_entry.get()]
                messagebox.showinfo('Info:',f'Email: {site['email']}\nPassword:{site['password']}')
            else:
                messagebox.showerror('Error', f'No details for "{website_entry.get()}" exists.')
    except FileNotFoundError:
        messagebox.showerror('Error', 'File not found')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = [letter for letter in LETTERS] + [symbol for symbol in SYMBOLS] + [number for number in NUMBERS]
    password = ''.join(sample(password_list, 10))

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror('Not enough data!','Some fields are missing')
        return
    is_ok = messagebox.askokcancel(title="Saving Data", message=f'The current data to be saved are:\nEmail: {website}\nPassword: {password}')
    if not is_ok: return

    new_data = {
        website.title() : {
            'email': email,
            'password': password
        }
    }

    try:
        with open(SAVE_LOCATION, 'r') as file:
                #Reading old data
            data = json.load(file)
                #Updating old data with new data
            data.update(new_data)
        with open(SAVE_LOCATION, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(SAVE_LOCATION, 'w') as file:
            json.dump(new_data, file, indent=4)
    finally:
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
website_entry = Entry(width=33)
website_entry.grid(row=2,column=1,sticky='w',columnspan=2)
search_button = Button(text='Search', command=find_password)
search_button.grid(row=2,column=2, sticky='we')

email_text = Label(text='Email/Username:')
email_text.grid(row=3,column=0)
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