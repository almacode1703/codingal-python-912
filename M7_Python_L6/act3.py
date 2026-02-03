# Rainbow using Turtle Graphics
import turtle
# creating canvas
turtle.Screen().bgcolor("Black")
sc = turtle.Screen()
sc.setup(800, 600)  
sc.title("Turtle Rainbow Drawing")
t = turtle.Turtle()
t.width(10)
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
t.penup()
t.goto(0, -200) 
t.pendown()
for color in colors:
    t.color(color)
    t.circle(200)
    t.penup()
    t.goto(0, -200 + (colors.index(color) + 1) * 10)  
    t.pendown()
turtle.done()