import turtle

# ---------- screen setup ----------
win = turtle.Screen()
win.setup(width=500, height=500)          # a tad larger than before
win.title("Pastel Rainbow Spiral")
win.bgcolor("#F6F8FF")                    # super-light sky blue background

# ---------- turtle setup ----------
t = turtle.Turtle()
t.hideturtle()                            # no arrow, just art
t.speed(0)                                # fastest rendering
t.width(4)

# gentle pastel rainbow (red → violet)
pastel_rainbow = [
    "#FF9AA2",  # pastel red
    "#FFB7B2",  # pastel orange
    "#FFDAC1",  # pastel yellow
    "#E2F0CB",  # pastel green
    "#B5EAD7",  # pastel turquoise
    "#C7CEEA",  # pastel indigo/violet
    "#F6C1FF"   # pastel pink-violet accent
]

# ---------- draw ----------
step = 10
angle = 59      # quirky angle gives a star-flower look

while True:
    t.pencolor(pastel_rainbow[step % len(pastel_rainbow)])
    t.forward(step)
    t.left(angle)
    step += 1
