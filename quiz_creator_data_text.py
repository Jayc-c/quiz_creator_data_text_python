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