import turtle

# Setup screen with aesthetic settings
screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("🌸 Aesthetic Turtle Window 🌸")
screen.bgcolor("#ffd1dc")  # soft pink background

# Create turtle with aesthetic style
pen = turtle.Turtle()
pen.shape("turtle")         # make the turtle visible
pen.color("#3b3c36")        # navy gray
pen.pensize(4)              # thicker lines
pen.speed(2)                # smooth drawing

# Draw a cute square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# End
turtle.done()
