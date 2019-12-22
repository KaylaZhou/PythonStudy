#!/usr/bin/python3

import turtle

turtle.screensize(400, 400, '#a9758b')  # 设置画布宽和高的大小,颜色
turtle.setup(400, 400, 0, 0)  # 设置画布窗口宽和高,以及坐标x,y的距离(距屏幕左上角的距离).
turtle.speed(1)  # 设置画笔移动的速度,(1-10)数字越大,速度越快.
turtle.pencolor('#ffaf50')  # 设置画笔的颜色

# 画笔运动命令:
turtle.pensize(10)  # 设置画笔的宽度
turtle.forward(100)     # 向当前画笔方向移动distance像素长
turtle.backward(50)     # 向当前画笔相反方向移动distance像素长
turtle.right(100)      # 顺时针移动 °
turtle.left(150)  # 逆时针移动 °
turtle.pendown()  # 移动时绘制图形,缺省时也为绘制
turtle.goto(10, 20)  # 将画笔移动到坐标为x,y的位置
turtle.penup()  # 移动时不绘制图形,提起笔，用于另起一个地方绘制时用
turtle.circle(50)  # 画圆,半径为正(负),表示圆心在画笔的左边(右边)画圆

# 画笔控制命令:
turtle.fillcolor('red')  # 绘制图形的填充颜色(箭头内部颜色)
turtle.color('red', '#72538e')  # 同时设置箭头颜色pencolor=color1, fillcolor=color2
turtle.filling()  # 返回当前是否在填充状态(无参数)
turtle.begin_fill()  # 准备开始填充图形(无参数)
turtle.end_fill()  # 填充完成
turtle.showturtle()  # *与hideturtle()函数对应*
turtle.hideturtle()  # 隐藏箭头显示

# 全局控制命令
turtle.clear()  # 清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset()  # 清空窗口，重置turtle状态为起始状态
turtle.undo()  # 撤销上一个turtle动作(注:无法撤销reset,clear)
turtle.isvisible()  # 返回当前turtle是否可见
# turtle.stamp()  # 复制当前图
# 三角形   (steps (optional) (做半径为radius的圆的内切正多边形,多边形边数为steps))
turtle.circle(80, steps=30)
turtle.circle(20, 80)  # 半圆


turtle.done()

#  python -m pip install --upgrade pip'pip升级命令'
