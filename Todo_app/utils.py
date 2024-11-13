# utils.py

import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt):
    """Get input from the user."""
    return input(prompt)
