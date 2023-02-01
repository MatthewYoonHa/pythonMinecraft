import turtle as t
n = 100

t.bgcolor("black")
colors = ["red", "yellow", "blue"]
t.speed(0)

for i in range(3):
    t.color(colors[i])
    t.forward(100)
    t.left(120)


    for x in range(n):
        t.circle(100)
        t.left(360/n)


"""t.color("green")
t.speed(0)
for x in range(n):
    t.circle(100)
    t.left(360/n)"""

t.exitonclick()