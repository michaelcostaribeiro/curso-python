import pandas
from tkinter import *
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 32,'italic')
WORD_FONT = ("Arial", 35,'bold')

FRONT_CARD_LOCATION = "images/card_front.png"
BACK_CARD_LOCATION = "images/card_back.png"
RIGHT_BUTTON_LOCATION = "images/right.png"
WRONG_BUTTON_LOCATION = "images/wrong.png"
DATA_LOCATION = "data/french_words.csv"
SAVE_LOCATION = "data/save.txt"

#Functions
def english_word_setup():
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=english_word, fill='white')
    canvas.itemconfig(background_image, image=flash_card_back_img)

def next_card():
    global after,french_word, english_word
    window.after_cancel(after)
    save_progress(english_word)
    r_index = randint(0, len(english_word_list)-1)
    french_word = french_word_list[r_index]
    english_word = english_word_list[r_index]
    canvas.itemconfig(language_text, text='French', fill=BACKGROUND_COLOR)
    canvas.itemconfig(word_text, text=french_word,fill=BACKGROUND_COLOR)
    canvas.itemconfig(background_image, image=flash_card_front_img)
    after = window.after(3000, english_word_setup)

def known_word():
    english_word_list.remove(english_word)
    french_word_list.remove(french_word)
    next_card()
    print(len(english_word_list))

#Saving progress
def load_progress(english_list):
    with open(SAVE_LOCATION, 'r') as file:
        progress = file.read().split(',')
    for item in progress:
        if item in english_list:
            english_list.remove(item)


def save_progress(word):
    with open(SAVE_LOCATION, 'a+') as save_file:
        current_progress = save_file.readlines()
        save_file.write(f'{word},')


#UI setup
window = Tk()
window.title("Flash Cards")
window.config(padx=100,pady=100,bg=BACKGROUND_COLOR)
flash_card_front_img = PhotoImage(file=FRONT_CARD_LOCATION)
flash_card_back_img = PhotoImage(file=BACK_CARD_LOCATION)
right_button_img = PhotoImage(file=RIGHT_BUTTON_LOCATION)
wrong_button_img = PhotoImage(file=WRONG_BUTTON_LOCATION)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
background_image = canvas.create_image(400,263,image=flash_card_front_img)
canvas.grid(row=0,column=0,columnspan=7)
language_text = canvas.create_text(400,140,text='French', font=LANGUAGE_FONT,fill=BACKGROUND_COLOR)
word_text = canvas.create_text(400,263,text='hello', font=WORD_FONT,fill=BACKGROUND_COLOR)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=1,column=1)

right_button = Button(image=right_button_img, highlightthickness=0, bd=0, command=known_word)
right_button.grid(row=1,column=5)

#loading progress


#pandas
data = pandas.read_csv(DATA_LOCATION)
french_word_list = data['French'].tolist()
english_word_list = data['English'].tolist()
load_progress(english_word_list)
random_index = randint(0,len(english_word_list))
french_word = french_word_list[random_index]
english_word = english_word_list[random_index]
canvas.itemconfig(word_text, text=french_word)
print(english_word_list)
print(len(english_word_list))

after = window.after(3000, english_word_setup)


window.mainloop()
