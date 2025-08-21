import tkinter as tk
import random

# 🎨 Colors & Fonts for Aesthetic Look
BG_COLOR = "#fdf6f0"
BTN_COLOR = "#ffb6b9"
BTN_HOVER = "#ff8b94"
TEXT_COLOR = "#333333"
FONT_TITLE = ("Poppins", 20, "bold")
FONT_BTN = ("Poppins", 14, "bold")
FONT_SCORE = ("Poppins", 12)

# Main Game Window
root = tk.Tk()
root.title("Rock Paper Scissors ✂️")
root.geometry("500x500")
root.configure(bg=BG_COLOR)

# Scores
player_score = 0
computer_score = 0

# 🎯 Game Logic
def play(choice):
    global player_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if choice == computer_choice:
        result = "It's a Tie! 😐"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
        player_score += 1
    else:
        result = "You Lose! 😢"
        computer_score += 1
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")

# 🏷 Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR)
title_label.pack(pady=20)

# 📜 Result Display
result_label = tk.Label(root, text="Choose your move!", font=FONT_SCORE, fg=TEXT_COLOR, bg=BG_COLOR)
result_label.pack(pady=20)

# 📊 Score Display
score_label = tk.Label(root, text="Player: 0  |  Computer: 0", font=FONT_SCORE, fg=TEXT_COLOR, bg=BG_COLOR)
score_label.pack(pady=10)

# 🎮 Buttons Frame
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=20)

# 🌟 Hover Effect
def on_enter(e):
    e.widget["bg"] = BTN_HOVER

def on_leave(e):
    e.widget["bg"] = BTN_COLOR

# 🪨📄✂️ Buttons
for move in ["Rock", "Paper", "Scissors"]:
    btn = tk.Button(frame, text=move, font=FONT_BTN, bg=BTN_COLOR, fg=TEXT_COLOR,
                    width=12, height=2, command=lambda m=move: play(m), relief="flat", bd=0)
    btn.pack(side="left", padx=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# 🚪 Exit Button
exit_btn = tk.Button(root, text="Exit Game", font=FONT_BTN, bg="#ff6666", fg="white",
                     width=15, height=2, command=root.destroy, relief="flat", bd=0)
exit_btn.pack(pady=30)

root.mainloop()
