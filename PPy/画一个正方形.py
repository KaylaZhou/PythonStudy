import turtle


def draw_square(w, h):

    turtle.screensize(w-50, h-50, '#de81ae')
    turtle.setup(w, h, 0, 0)
    turtle.pensize(3)
    turtle.speed(1)


draw_square(350, 350)

turtle.color('#fcfdaf', '#8d2e4c')   # 设置画笔和填充的颜色
turtle.begin_fill()  # 开始填充

for a in range(0, 4):

    turtle.forward(150)
    turtle.right(90)

turtle.end_fill()     # 填充完成
turtle.hideturtle()  # 隐藏箭头显示

turtle.done()
