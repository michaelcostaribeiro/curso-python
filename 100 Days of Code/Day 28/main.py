from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MINUTE = 60

CHECKMARK_SYMBOL = '✔'
reps = 0
restarting = False
timer = 'reset'


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    pomo_timer.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
    canvas.itemconfig(timer_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    pomo_timer.config(text='Work', fg=GREEN)
    countdown(WORK_MIN * MINUTE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time_in_seconds):
    global reps, timer
    seconds = time_in_seconds % 60
    minutes = int(time_in_seconds/60)

    canvas.itemconfig(timer_text, text=f'{minutes:02d}:{seconds:02d}')

    if seconds == 0 and minutes == 0:
        reps += 1
        if reps == 8:
            time_in_seconds = LONG_BREAK_MIN * MINUTE
            checkmark.config(text=CHECKMARK_SYMBOL + checkmark['text'])
            pomo_timer.config(text='Break', fg=PINK)
            if reps > 8:
                return
        elif reps % 2 == 0:
            time_in_seconds = SHORT_BREAK_MIN * MINUTE
            pomo_timer.config(text='Break', fg=RED)
            checkmark.config(text=CHECKMARK_SYMBOL + checkmark['text'])
        elif reps % 2 != 0:
            pomo_timer.config(text='Work', fg=GREEN)
            time_in_seconds = WORK_MIN * MINUTE



    timer = window.after(1000, countdown, time_in_seconds-1)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

pomo_timer = Label(text='Timer', bg=YELLOW, fg=GREEN,font=(FONT_NAME,50))
pomo_timer.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103,130, text='00:00', font=(FONT_NAME,30,'bold'), fill="white")
canvas.grid(row=1,column=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2,column=0)


restart_button = Button(text='Restart', command=reset)
restart_button.grid(row=2,column=2)

checkmark = Label(text='', bg=YELLOW, fg=GREEN,font=(FONT_NAME,16, 'bold'))
checkmark.grid(row=3,column=1)





window.mainloop()
