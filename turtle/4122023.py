import turtle as t

t.shape("turtle")
t.color("red")
t.pensize(width=5)

t.begin_fill()

sideLength = 50
angle = 72
for i in range(0, 5):
    t.forward(sideLength)
    t.right(angle)

t.end_fill()

t.exitonclick()