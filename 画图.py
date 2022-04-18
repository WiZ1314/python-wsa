# coding:utf-8
# 工程文件:python-wsa
# 代码文件:画图
# 创建时间:2022/4/11 10:21
import turtle as t

t.speed(10)


def hongqi():
	t.setup(600, 400, 0, 0)
	t.bgcolor("red")
	t.fillcolor("yellow")
	t.color('yellow')
	t.speed(5)
	t.begin_fill()
	t.up()
	t.goto(-280, 100)
	t.down()
	for i in range(5):
		t.forward(150)
		t.right(144)
	t.end_fill()
	t.begin_fill()
	t.up()
	t.goto(-100, 180)
	t.setheading(305)
	t.down()
	for i in range(5):
		t.forward(50)
		t.left(144)
	t.end_fill()
	t.begin_fill()
	t.up()
	t.goto(-50, 110)
	t.setheading(30)
	t.down()
	for i in range(5):
		t.forward(50)
		t.right(144)
	t.end_fill()
	t.begin_fill()
	t.up()
	t.goto(-40, 50)
	t.setheading(5)
	t.down()
	for i in range(5):
		t.forward(50)
		t.right(144)
	t.end_fill()
	t.begin_fill()
	t.up()
	t.goto(-100, 10)
	t.setheading(300)
	t.down()
	for i in range(5):
		t.forward(50)
		t.left(144)
	t.end_fill()
	t.hideturtle()


def wuhuan():
	t.width(5)  # 控制画笔宽度
	colors = ['blue', 'black', 'red', 'yellow', 'green']
	for i in range(5):
		t.color(colors[i])  # 控制画笔颜色
		t.circle(50)  # 控制圆的大小，半径
		t.penup()  # 让画笔抬起
		if i <= 1:
			t.goto((i + 1) * 120, 0)
			t.pendown()
		elif i == 2:
			t.goto(60, -30)
			t.pendown()
		elif i == 3:
			t.goto(180, -30)
			t.pendown()
		else:
			t.color('green')
			t.circle(50)
	t.hideturtle()


def fangkuai():
	t.fillcolor('yellow')
	t.begin_fill()
	while 1:
		t.forward(200)  # 向前走200
		t.right(90)  # 向右转144度
		if abs(t.pos()) < 1:
			break
	t.end_fill()


def hua():
	t.Pen()
	t.bgcolor("black")
	sides = 6
	colors = ["red", "yellow", "green", "blue", "orange", "purple"]
	for x in range(360):
		t.pencolor(colors[x % sides])
		t.forward(x * 3 / sides + x)
		t.left(360 / sides + 1)
		t.width(x * sides / 200)


def liang():
	t.Pen()
	t.bgcolor("black")
	sides = int(input("输入要绘制的边的数目，请输入2-6的数字！"))
	colors = ["red", "yellow", "green", "blue", "orange", "purple"]
	for x in range(100):
		t.pencolor(colors[x % sides])
		t.forward(x * 3 / sides + x)
		t.left(360 / sides + 1)
		t.width(x * sides / 200)


def xiaozhu():
	t.Pen()
	t.setting()  # 画布、画笔设置
	t.nose(-100, 100)  # 鼻子
	t.head(-69, 167)  # 头
	t.ears(0, 160)  # 耳朵
	t.eyes(0, 140)  # 眼睛
	t.cheek(80, 10)  # 腮
	t.mouth(-20, 30)  # 嘴
	t.body(-32, -8)  # 身体
	t.hands(-56, -45)  # 手
	t.foot(2, -177)  # 脚
	t.tail(148, -155)  # 尾巴


wuhuan()
t.done()
