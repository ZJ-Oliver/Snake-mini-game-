import turtle
import time
import random

# 设置游戏屏幕
window = turtle.Screen()
window.title("贪吃蛇游戏")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # 关闭自动更新

# 贪吃蛇的头部
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 身体部分列表
segments = []

# 分数显示
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("分数: 0", align="center", font=("Courier", 24, "normal"))


# 函数：改变方向
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# 函数：蛇的移动
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# 绑定键盘事件
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

# 游戏主循环
while True:
    window.update()

    # 检查是否撞墙
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # 隐藏身体部分
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        pen.clear()
        pen.write("分数: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # 检查是否吃到食物
    if head.distance(food) < 20:
        # 随机放置食物
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # 增加身体部分
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # 增加分数
        score += 10
        pen.clear()
        pen.write("分数: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # 移动身体部分（从尾部向前移动）
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # 移动第一个身体部分到头部位置
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 检查是否撞到自己
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            pen.clear()
            pen.write("分数: {}".format(score), align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)
