# Using turtle draw a square with each side of length 100 units.
import turtle   

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(500, 500)

sc.title("Turtle Square Drawing")
# turtle.title("Square with Turtle")

t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
    i += 1

turtle.done()