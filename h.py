import tkinter as tk
import random
from tkinter import messagebox

def spele():
    return [
        ("Cor", ["Sirds", "Liver", "Plaušas"], "Sirds"),
        ("Hepat", ["Stomach", "Liver", "Smadzenes"], "Liver"),
        ("Pulmo", ["Plaušas", "Kidney", "Intestine"], "Plaušas"),
        ("Cerebrum", ["Smadzenes", "Sirds", "Spine"], "Smadzenes"),
        ("Ren", ["Liver", "Kidney", "Pancreas"], "Kidney")
    ]

def check_answer(selected_option, correct_answer, root):
    if selected_option.get() == correct_answer:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Wrong! The correct answer was {correct_answer}.")
    root.quit()

def play_game():
    quiz_data = spele()
    random.shuffle(quiz_data)
    
    for latin_name, options, correct_answer in quiz_data:
        root = tk.Tk()
        root.title("Guess the Human Organ")
        
        tk.Label(root, text="Latīniskais nosaukums orgānam", font=("Arial", 14)).pack(pady=10)
        tk.Label(root, text=latin_name, font=("Arial", 12)).pack(pady=5)
        
        selected_option = tk.StringVar(value="")
        
        for option in options:
            tk.Radiobutton(root, text=option, variable=selected_option, value=option, font=("Arial", 12)).pack(anchor="w")
        
        tk.Button(root, text="Pareizi/nepareizi!", font=("Arial", 12), 
                  command=lambda: check_answer(selected_option, correct_answer, root)).pack(pady=10)
        
        root.mainloop()

if __name__ == "__main__":
    play_game()