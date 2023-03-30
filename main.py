from turtle import Turtle, Screen
import turtle as t
import colorgram
import random

turtle = Turtle()
screen = Screen()

turtle.hideturtle()

# Extract the colors from the image loaded
colors = colorgram.extract('nature.jpg', 6)

# List to save all the colors extracted from the image
rgb_colors = []

# Save the colors in rbg_colors list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Activate RGB color
t.colormode(255)

# Hide lines and set up the speed
turtle.penup()
turtle.speed(0)

# Initialize patter in a specific position
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

# Get x,y position
x_position = int(turtle.xcor())
y_position = int(turtle.ycor())

# Function that will create the matrix
def dots_matrix(turtle, x, y, times):
    for _ in range(times):
        for _ in range(times):
            color = random.choice(rgb_colors)

            turtle.dot(20, color)
            turtle.forward(50)

        y += 50
        turtle.goto(x, y)


dots_matrix(turtle, x_position, y_position, 10)
screen.exitonclick()