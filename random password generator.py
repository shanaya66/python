import tkinter as tk
from tkinter import messagebox
import random
import string

# 🎨 Colors & Fonts
BG_COLOR = "#f5f5f5"
BTN_COLOR = "#c3aed6"
BTN_HOVER = "#8675a9"
TEXT_COLOR = "#333333"
FONT_TITLE = ("Poppins", 20, "bold")
FONT_BTN = ("Poppins", 14, "bold")
FONT_LABEL = ("Poppins", 12)

# Main Window
root = tk.Tk()
root.title("Random Password Generator 🔑")
root.geometry("500x400")
root.configure(bg=BG_COLOR)

# Generate Password Function
def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
    check_strength(password)

# Password Strength Checker as:shshh
def check_strength(password):
    strength = "Weak 😢"
    color = "red"
    
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong 💪"
        color = "green"
    elif len(password) >= 6:
        strength = "Medium 🙂"
        color = "orange"
    
    strength_label.config(text=f"Strength: {strength}", fg=color)

# Copy to Clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Hover Effect
def on_enter(e):
    e.widget["bg"] = BTN_HOVER

def on_leave(e):
    e.widget["bg"] = BTN_COLOR

# Title
title_label = tk.Label(root, text="Random Password Generator", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR)
title_label.pack(pady=20)

# Password Display
password_entry = tk.Entry(root, font=FONT_LABEL, width=30, bd=2, relief="flat", justify="center")
password_entry.pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", font=FONT_LABEL, bg=BG_COLOR)
strength_label.pack(pady=5)

# Length Input
length_var = tk.IntVar(value=8)
length_frame = tk.Frame(root, bg=BG_COLOR)
length_frame.pack(pady=10)

tk.Label(length_frame, text="Password Length:", font=FONT_LABEL, bg=BG_COLOR).pack(side="left", padx=5)
length_entry = tk.Entry(length_frame, textvariable=length_var, width=5, font=FONT_LABEL, justify="center")
length_entry.pack(side="left")

# Buttons
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=20)

generate_btn = tk.Button(btn_frame, text="Generate", font=FONT_BTN, bg=BTN_COLOR, fg="white",
                         width=12, command=generate_password, relief="flat", bd=0)
generate_btn.pack(side="left", padx=10)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

copy_btn = tk.Button(btn_frame, text="Copy", font=FONT_BTN, bg=BTN_COLOR, fg="white",
                     width=12, command=copy_password, relief="flat", bd=0)
copy_btn.pack(side="left", padx=10)
copy_btn.bind("<Enter>", on_enter)
copy_btn.bind("<Leave>", on_leave)

# Exit Button
exit_btn = tk.Button(root, text="Exit", font=FONT_BTN, bg="#ff6666", fg="white",
                     width=15, command=root.destroy, relief="flat", bd=0)
exit_btn.pack(pady=10)

root.mainloop()
