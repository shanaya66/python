from tkinter import *

win = Tk()
win.geometry("450x450")
win.title("Gradient Grid GUI")
win.configure(bg="#fdf6f0")  # Cream background for aesthetic look

# Aesthetic Frame
frame1 = Frame(win, relief='flat', bg="#ffeaa7", bd=3, padx=20, pady=20)
frame1.grid(row=0, column=0, padx=40, pady=40)

# Custom pastel colors for gradient-style effect
pastel_colors = [
    "#fab1a0", "#fbc531", "#55efc4",
    "#81ecec", "#74b9ff", "#a29bfe",
    "#ffeaa7", "#fd79a8", "#e17055"
]

# Create grid of labels with gradient color effect
count = 0
for i in range(3):
    for j in range(3):
        label1 = Label(frame1,
                       relief='groove',
                       text=f"row {i}, col {j}",
                       bg=pastel_colors[count % len(pastel_colors)],
                       fg="#2d3436",
                       font=('Helvetica', 11, 'bold'),
                       width=14,
                       height=2,
                       bd=1)
        label1.grid(row=i, column=j, padx=8, pady=8)
        count += 1

win.mainloop()
