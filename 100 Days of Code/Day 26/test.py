import random

numbers_array = [1,2,3,4,5]
new_numbers_array = [number+1 for number in numbers_array if number%2==0]
print(new_numbers_array)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for student, score in students_scores.items() if score>=60}
print('These are the passed students:')
print(passed_students)

# for key, value in d.items():

