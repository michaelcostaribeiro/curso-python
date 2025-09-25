import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN_BUTTON_PATH = 'images/true.png'
RED_BUTTON_PATH = 'images/false.png'
FONT = ('Arial',20,'italic')

class Ui:
    def __init__(self, quiz_brain:QuizBrain):
        self.window = tk.Tk()
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.window.title('Quiz gaming')
        self.quiz = quiz_brain
        self.current_question = self.quiz.next_question()
        self.score = 0

        #row 0
        self.score_label = tk.Label(self.window, text=f'Score: {self.score}', bg=THEME_COLOR, fg='white',pady=10)
        self.score_label.grid(row=0,column=1)

        #row 1
        self.canvas = tk.Canvas(self.window, width=300,height=250, bg='white')
        self.question = self.canvas.create_text(150,125,text=self.current_question,font=FONT,fill=THEME_COLOR,width=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=10)

        #row 2
        self.green_button_img = tk.PhotoImage(file=GREEN_BUTTON_PATH)
        self.green_button = tk.Button(self.window, image=self.green_button_img,command=self.true_answer)
        self.green_button.grid(row=2, column=0,pady=20)

        self.red_button_img = tk.PhotoImage(file=RED_BUTTON_PATH)
        self.red_button = tk.Button(self.window, image=self.red_button_img,command=self.false_answer)
        self.red_button.grid(row=2, column=1)


        self.window.mainloop()

    #ui_brain
    def true_answer(self):
        self.quiz.check_answer('True')
        self.update_score()
        self.next_question()

    def false_answer(self):
        self.quiz.check_answer('False')
        self.update_score()
        self.next_question()

    def update_score(self):
        self.score = self.quiz.score
        self.score_label.config(text=f'Score: {self.score}')

    def next_question(self):
        self.current_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=self.current_question)




