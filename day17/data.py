question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
def quiz():
    number_questoins = 0 
    score =0
    while number_questoins < len(question_data):
        
        for question in question_data:   
            user_input = input(f'{question['text']} (True or False) : \n').capitalize()
            if user_input == question["answer"]:
                if number_questoins == len(question_data):
                    return f'Congrats you have answered all the Questions'
                
                score += 1
                print(f' you got it rigth \n the correct answer is : {question["answer"]}')
                print(f'your current score is {score}/{score} ')
                number_questoins+=1
                
            else:
                print(f'Thats wrong \nthe correct answer was : {question["answer"]}')
                return f'your current score is {score}/{score+1}'
        

print(quiz())
