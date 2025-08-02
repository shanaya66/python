from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("Aesthetic Tkinter UI")
win.configure(bg="#fdf6f0")  # soft cream background

# Aesthetic Label
label1 = Label(win, text="Name", bg="#fdf6f0", fg="#6c5ce7", font=('Helvetica', 12, 'bold'))
label1.pack(pady=8)

# Aesthetic Entry
entry1 = Entry(win, bg="#ffeaa7", fg="#2d3436", relief=FLAT, font=('Helvetica', 11))
entry1.pack(pady=4, ipadx=10, ipady=4)

# Aesthetic Button
button1 = Button(win, text="Click Me", bg="#81ecec", fg="#2d3436", activebackground="#00cec9",
                 font=('Helvetica', 11, 'bold'), relief=FLAT, padx=10, pady=4)
button1.pack(pady=10)

# Aesthetic Frame
frame1 = Frame(win, width=300, height=100, bg="#ffeaa7", bd=0)
frame1.pack(pady=10)

# Label inside frame
label2 = Label(frame1, text="Login", fg="#d63031", bg="#ffeaa7", font=('Helvetica', 11, 'italic'))
label2.pack(pady=5)

# Aesthetic Text box inside frame
text1 = Text(frame1, bg="#fab1a0", fg="#2d3436", font=('Courier', 10),
             width=30, height=4, relief=FLAT, bd=5)
text1.pack(pady=5)

win.mainloop()
