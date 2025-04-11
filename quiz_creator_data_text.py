# import modules
import json 
import os 

# Create a function to get a valid answer.
def get_valid_answer(prompt):
    # Ask the user for the answer (a, b, c, or d) and make sure it's valid.
    while True:
        answer = input(f"{prompt} (a, b, c, d): ").lower() 
        if answer in ['a', 'b', 'c', 'd']: 
            return answer 
        else: 
            print("Invalid input. Please enter 'a', 'b', 'c', or 'd' ONLY.") 

# Create a function to create the quiz
def create_quiz():
    # Get the questions and answers from the user and save them to a file.
    filename = "quiz_data.txt" 
    questions = [] 