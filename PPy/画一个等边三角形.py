import turtle


def create_canvas(w, h):
    turtle.screensize(w-2, h-2, '#b64c5a')
    turtle.setup(w, h, 30, 30)
    turtle.speed(1)


create_canvas(300, 300)

for i in range(0, 3):

    turtle.forward(80)
    turtle.right(180-180/3)


turtle.done()
