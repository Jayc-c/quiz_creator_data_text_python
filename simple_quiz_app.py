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

