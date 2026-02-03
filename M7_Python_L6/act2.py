# Draw Star with turtle graphics
import turtle
# creating canvas
turtle.Screen().bgcolor("LightBlue")
sc = turtle.Screen()
sc.setup(500, 500)
sc.title("Turtle Star Drawing")
t = turtle.Turtle()
for i in range(5):
    t.forward(150)
    t.right(144)
    i += 1  
turtle.done()