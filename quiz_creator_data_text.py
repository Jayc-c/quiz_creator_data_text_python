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

    print("\n WELCOME TO THE QUIZ CREATOR! ")
    print("Be creative, and don't be afraid to make some great questions!\n")

    # Create an infinite loop to keep asking the user for question.
    # Until they decided to stop.
    while True: 
        print("-" * 47) 
        question = input("Enter your question (or type 'exit' to finish):\n")
        if question.lower() == 'exit': 
            break
        
        # Create a place to store the answer choices provided by the user (a, b, c, d).
        options = {} 
        print("\nEnter the possible answers:") 
        options['a'] = input("a) ") 
        options['b'] = input("b) ") 
        options['c'] = input("c) ") 
        options['d'] = input("d) ") 

        # Ask the user to input the correct answer (a, b, c, or d)
        correct_answer = get_valid_answer("Enter the letter of the correct answer: ") 

        # Compile the question, options, and correct answer together to the questions list.
        questions.append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        })

    # Check if questions exist and save them to a JSON file,
    # handling errors and empty lists.
    if questions: 
        try: 
            with open(filename, 'w') as outfile: 
                json.dump(questions, outfile, indent=4) 
            print(f"\n Done! Your questions are now saved in '{filename}'!")
        except Exception as e:
            print(f" Oops! Couldn't save the file: {e}")
    else: # If the user didn't add any questions.
        print("\n😴 No questions added.")

create_quiz()