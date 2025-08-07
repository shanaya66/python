from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.geometry("400x400")
window.title("💻 Message Box Window")
window.config(bg='#a8dadc')  # pastel blue background

# Optional: Set a custom icon (must be .ico file and in same folder)
# Uncomment the line below and make sure 'icon.ico' exists
# window.iconbitmap("icon.ico")

# Define the message box function
def msg():
    messagebox.showwarning("⚠️ Alert", "🚨 Virus Found!!! Please scan your system.")

# Create a styled aesthetic button
button1 = Button(
    window,
    text='Click Me',
    command=msg,
    font=("Helvetica", 14, "bold"),
    bg='#f1faee',        # light pastel background
    fg='#1d3557',        # deep blue text
    activebackground='#bde0fe',
    activeforeground='#1d3557',
    relief='raised',
    bd=3,
    padx=10,
    pady=5,
    highlightthickness=2,
    highlightbackground="#457b9d",
    cursor="hand2"
)

# Place the button in the window
button1.place(x=135, y=170)

# Run the window loop
window.mainloop()
