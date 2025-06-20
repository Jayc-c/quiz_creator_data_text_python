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