#dictionary comprehension
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
import random

students_scores = {students : random.randint(50,100) for students in names }
print(students_scores)

passed_students = {student : score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)