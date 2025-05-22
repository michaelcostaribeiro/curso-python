
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, answer):
        return answer == self.question_list[self.question_number].answer.lower()

    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)").lower()
        is_correct = self.check_answer(answer)
        self.question_number += 1
        return is_correct

    def still_has_question(self):
        print(f'Your current score is: {self.score}/{len(self.question_list)}')
        return self.question_number<len(self.question_list)
