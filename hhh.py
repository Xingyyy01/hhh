import turtle as T
import random
import time




def Tree(branch, t):
    time.sleep(0.005)
    if branch > 3:
        if branch >= 8 and branch <= 12:
            if random.randint(0, 3) == 0:
                t.color('tomato')#红色
            elif random.randint(0, 3) == 1:
                t.color('mediumturquoise')  # 蓝色
            else:
                t.color('lightsalmon')#橙色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 2) == 0:
                t.color('mediumslateblue')  # 紫色
            elif random.randint(0, 2) == 1:
                t.color('lightgreen')#绿色
            else:
                t.color('gold')#黄色
            t.pensize(branch / 2)
        else:
            t.color('sienna')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        if random.randint(0, 5) == 0:
            t.color('indianred')  # 红色，淡珊瑚色lightcoral
        if random.randint(0, 5) == 1:
            t.color('lightpink')  # 粉色
        if random.randint(0, 5) == 2:
            t.color('lightgreen')  # 绿色
        if random.randint(0, 5) == 3:
            t.color('mediumturquoise')  # 蓝色
        if random.randint(0, 5) == 4:
            t.color('mediumslateblue')  # 紫色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


t = T.Turtle()

w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

printer = T.Turtle()
printer.hideturtle()
printer.penup()
printer.back(200)
printer.write("祝你充实快乐每一天!\n\n", align="center", font=("楷体", 16, "bold"))

printer.write("           Wish you full and happy everyday!", align="center", font=("Courier", 12, "normal"))

Tree(60, t)

Petal(200, t)
w.exitonclick()
