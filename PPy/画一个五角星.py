import turtle


def draw_square(w, h):

    turtle.screensize(w-20, h-20, '#de81ae')
    turtle.setup(w, h, 10, 0)
    turtle.pensize(2)
    turtle.speed(2)


draw_square(450, 450)

for _ in range(5):

    turtle.forward(180)
    turtle.right(180-36)


turtle.hideturtle()

turtle.done()
