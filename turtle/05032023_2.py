import turtle as t

t.shape("arrow")
t.bgcolor("black")
t.color("pink")
t.pensize(width=3)
t.speed(0)

n = 10
colors = ["red", "yellow", "blue"]

for i in range(3):
    t.color(colors[i])
    t.left(120)
    for x in range(n):
        t.circle(100)
        t.left(360/n)

t.exitonclick()
