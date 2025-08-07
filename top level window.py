from tkinter import *

# Function to create a toplevel window
def toplevel():
    toplevel1 = Toplevel(window)
    toplevel1.geometry('200x200')
    toplevel1.title("TOP LEVEL")
    toplevel1.configure(bg='cyan')

    label2 = Label(
        toplevel1,
        text="THIS IS THE toplevel WINDOW"
    )
    label2.pack()

# Root window
window = Tk()

label1 = Label(
    window,
    text="THIS IS THE ROOT WINDOW"
)
label1.place(x=100, y=200)

button1 = Button(
    window,
    text="click me",
    command=toplevel
)
button1.place(x=100, y=240)

window.mainloop()
