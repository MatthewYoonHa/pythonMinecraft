import turtle as t


t.bgcolor("black")
t.speed(0)

n = 100
colors = ["green", "red", "blue"]

for i in range(3):
    t.forward(100)
    t.left(120)
    t.color(colors[i])

    for x in range(n):
        t.circle(50)
        t.left(360/n)

t.exitonclick()