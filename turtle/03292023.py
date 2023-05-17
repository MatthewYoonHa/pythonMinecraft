import turtle as t

# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
t.shape("turtle")
# color, fillcolor, pencolor
t.color("red")
t.pensize(width=5)

# color filled square
t.begin_fill()
#
t.forward(50)
# t.fd(50)

t.right(90)
# t.rt(90)

t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)

# color filled end
t.end_fill()

# stay open window and exit on mouse Click
t.exitonclick()