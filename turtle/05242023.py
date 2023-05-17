import turtle as t

leng = 40
for i in range(-200, 200, 100):
    for j in range(-200, 200, 100):
        t.pu()
        t.goto(i, j)
        t.pd()
        t.circle(leng)

t.exitonclick()
