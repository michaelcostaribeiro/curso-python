from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for i in range(0,len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))

quiz = QuizBrain(question_bank)

finished = True

while finished:
    if quiz.still_has_question():
        correctAnswer = quiz.next_question()
        if correctAnswer:
            quiz.score += 1
            print('Correct!')
        else:
            print('Wrong!')
    else:
        finished = False

print(f'Final score: {quiz.score}/{len(quiz.question_list)}')
