# List of student names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random

# Create a dictionary with student names as keys and random scores between 50 and 100 as values
students_scores = {students: random.randint(50, 100) for students in names}
print(students_scores)

# Create a new dictionary with only the students who scored 60 or above
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


#looping through rows of a dataframe using iterows()
