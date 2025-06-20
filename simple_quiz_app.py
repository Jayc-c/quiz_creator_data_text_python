# import necessary modules.
import tkinter as tk
from tkinter import messagebox 
import json 
import time 
import random 

# created a function to load the quiz questions from the JSON file.
def load_quiz_from_file(filename):
    try:
        # open and load JSON data.
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # handle missing file.
        messagebox.showerror("Error", f"File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        # handle invalid JSON.
        messagebox.showerror("Error", "Invalid quiz file format.")
        return []

# created the main function to run the quiz GUI.
def run_quiz_gui(quiz_file):
    window = tk.Tk()            
    window.title("Simple Quiz")

    quiz_questions = load_quiz_from_file(quiz_file)
    if not quiz_questions:
        return

    current_question_index = 0  # track current question.
    score = 0                   # user's score.
    start_time = 0              # quiz start time.

    # created function to update and display quiz timer.
    def update_timer():
        if start_time and quiz_questions:
            elapsed = time.time() - start_time
            label_time.config(text=f"Time: {elapsed:.1f} seconds")
        window.after(100, update_timer)

    # created another function to display current question and options.
    def show_question():
        nonlocal current_question_index
        if 0 <= current_question_index < len(quiz_questions):
            question_data = quiz_questions[current_question_index]
            label_question.config(text=question_data.get('question', ''))
            options = question_data.get('options', {})
            option_keys = list(options.keys())

            if len(option_keys) == 4:
                # Configure and show radio buttons.
                for i in range(4):
                    radio_buttons[i].config(text=f"{option_keys[i].upper()}. {options[option_keys[i]]}", value=option_keys[i])
                    radio_buttons[i].pack(anchor=tk.W)
                answer_var.set(None)             # Clear selection.
                label_result.config(text="")     # Clear previous result.
                button_next.config(state=tk.DISABLED) # Disable next until answer.
                for rb in radio_buttons:         # Enable radio buttons.
                    rb.config(state=tk.NORMAL)
                button_submit.config(state=tk.NORMAL) # Enable submit.
            else:
                label_question.config(text="Error: Question format incorrect (missing options).")
        else:
            show_results() # Show results if no more questions.

    # Check the selected answer.
    def check_answer():
        nonlocal score
        if 0 <= current_question_index < len(quiz_questions):
            question_data = quiz_questions[current_question_index]
            correct_answer = question_data.get('correct_answer', '').lower()
            user_answer = answer_var.get()
            
            # Compare and update score/feedback.
            if user_answer == correct_answer:
                label_result.config(text="Correct!", fg="green")
                score += 1
            else:
                options = question_data.get('options', {})
                correct_text = options.get(correct_answer, "N/A")
                label_result.config(text=f"Wrong! Correct answer: {correct_text}", fg="red")
            
            button_next.config(state=tk.NORMAL) # Enable next.
            for rb in radio_buttons:             # Disable options.
                rb.config(state=tk.DISABLED)
            button_submit.config(state=tk.DISABLED) # Disable submit.

    # Advance to the next question.
    def next_question():
        nonlocal current_question_index
        current_question_index += 1
        show_question()
