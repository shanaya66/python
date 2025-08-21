import tkinter as tk
from tkinter import messagebox
import random

# Colors
BG_COLOR = "#fcefee"   # pastel pink background
BTN_COLOR = "#c1e1dc"  # pastel mint green
BTN_HOVER = "#a8d8cd"
TEXT_COLOR = "#3c3c3c" # dark grey
RESULT_COLOR = "#f9d5e5" # pastel peach

# Game choices
choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win 🎉"
    else:
        result = "Computer Wins 😢"

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n\n{result}")

# Hover effect
def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e):
    e.widget['background'] = BTN_COLOR

# Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors - Aesthetic GUI")
root.geometry("450x400")
root.configure(bg=BG_COLOR)

# Heading
heading = tk.Label(root, text="Rock Paper Scissors", font=("Comic Sans MS", 20, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
heading.pack(pady=15)

# Buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=("Comic Sans MS", 14, "bold"),
                    bg=BTN_COLOR, fg=TEXT_COLOR, width=10, relief="flat",
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=10)

    # Bind hover effect
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Result display
result_label = tk.Label(root, text="", font=("Comic Sans MS", 14),
                        bg=RESULT_COLOR, fg=TEXT_COLOR, relief="solid", bd=2, padx=10, pady=10)
result_label.pack(pady=20)

# Exit button
exit_btn = tk.Button(root, text="Exit", font=("Comic Sans MS", 12, "bold"),
                     bg="#f4c2c2", fg=TEXT_COLOR, width=10, relief="flat", command=root.quit)
exit_btn.pack(pady=10)

root.mainloop() 
