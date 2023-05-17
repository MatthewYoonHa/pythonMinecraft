import turtle

turtle.setup(width=950, height=300)
t = turtle.Turtle()
t.shape('turtle')

polygons = [(-400, 0, "red"), (-300, 3, "orange"), (-200, 4, "yellow"), (-100, 5, "green"),
            (0, 6, "blue"), (100, 7, "purple"), (200, 8, "orange"), (300, 9, "green")]

for polygon in polygons:
    t.penup()
    t.goto(polygon[0], -50)
    t.color(polygon[2])
    t.pendown()
    if polygon[1] == 0:
        t.circle(50)
    else:
        t.circle(50, steps=polygon[1])

turtle.exitonclick()
