import turtle


def create_canvas(w, h):
    turtle.screensize(w-2, h-2, '#b64c5a')
    turtle.setup(w, h, 30, 30)
    turtle.speed(1)


create_canvas(300, 300)
# turtle.forward(70)
# turtle.circle(50, steps=3)


turtle.done()
