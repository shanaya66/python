# 🌸 Aesthetic Pastel Star with Gradient Effect ✨

import turtle

# 🎨 Setup Screen
screen = turtle.Screen()
screen.screensize(400, 400)
screen.bgcolor("#E0F7FA")  # soft pastel blue

# 🐢 Create the Turtle
star = turtle.Turtle()
star.speed(3)
star.width(6)

# 🌈 Define pastel gradient colors
pastel_gradient = ["#F8BBD0", "#F48FB1", "#CE93D8"]  # light pink → orchid purple

# 💫 Draw the first triangle (left turn)
for i in range(3):
    star.color(pastel_gradient[i])
    star.forward(100)
    star.left(120)

# 🛸 Move to a new position for second triangle
star.penup()
star.left(90)
star.forward(60)
star.right(90)
star.pendown()

# 💫 Draw the second triangle (right turn)
for i in range(3):
    star.color(pastel_gradient[2 - i])  # reverse the gradient
    star.forward(100)
    star.right(120)

# ✨ End Drawing
star.hideturtle()
turtle.done()
