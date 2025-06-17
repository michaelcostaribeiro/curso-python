from tkinter import *



window = Tk()
window.title('finally GUI')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label

my_label = Label(text='test label'.upper(), font=('Courier', 20))

my_label['text'] = "New Text"
my_label.config(text='New text')
my_label.grid(column=0,row=0)

#button

new_button = Button(text='new button')
new_button.grid(column=2, row=0)

button = Button(text='Clickable')
button.grid(column=1,row=1)

#entry
entry = Entry()
entry.grid(column=3,row=2)
window.mainloop()