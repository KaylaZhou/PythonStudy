import turtle


def draw_square(w, h):

    turtle.screensize(w-30, h-30, '#de81ae')
    turtle.setup(w, h, 10, 0)
    turtle.pensize(2)
    turtle.speed(1)


draw_square(600, 600)

turtle.color('#b64a59', '#860e01')
turtle.begin_fill()

turtle.left(135)
turtle.circle(100, 180)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.circle(100, 180)
turtle.end_fill()

turtle.penup()   # 移动箭头时, 不会绘制图形
turtle.goto(150, -280)  # 将画笔移动至x,y坐标


turtle.write("Kayla周", font=("楷体", 26, "normal"))
# turtle.write("内容", font=("楷体", 大小, "类型"))

turtle.hideturtle()


turtle.done()
