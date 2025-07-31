# 🌸 Pastel Shapes Wonderland using Turtle 🐢

import turtle

# Setup Screen
screen = turtle.Screen()
screen.title("🌸 Pastel Shapes Wonderland 🌸")
screen.bgcolor("mistyrose")

# Create turtle
pen = turtle.Turtle()
pen.pensize(4)
pen.speed(2)

# --- Shape Functions with Pastel Colors ---
def draw_triangle():
    pen.color("plum")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()

def draw_rectangle():
    pen.color("powderblue")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(140)
        pen.left(90)
        pen.forward(80)
        pen.left(90)
    pen.end_fill()

def draw_hexagon():
    pen.color("lightgreen")
    pen.begin_fill()
    for _ in range(6):
        pen.forward(70)
        pen.left(60)
    pen.end_fill()

def draw_circle():
    pen.color("peachpuff")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

# --- Drawing Layout with Spacing ---

# Triangle ✨
pen.penup()
pen.goto(-250, 100)
pen.pendown()
draw_triangle()

# Rectangle ✨
pen.penup()
pen.goto(-50, 100)
pen.pendown()
draw_rectangle()

# Hexagon ✨
pen.penup()
pen.goto(180, 100)
pen.pendown()
draw_hexagon()

# Circle ✨
pen.penup()
pen.goto(-40, -50)
pen.pendown()
draw_circle()

# Hide turtle at the end
pen.hideturtle()

# Done 🎀
turtle.done()

