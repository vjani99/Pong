# Simple Pong in Python 3
# By Vedant Jani

import turtle
import time
import os

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600, startx=300, starty=50)
win.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6

# Scoreboard (pen)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Countdown (pen)
cd_pen = turtle.Turtle()
cd_pen.speed(0)
cd_pen.color("white")
cd_pen.penup()
cd_pen.hideturtle()
cd_pen.goto(0, 0)


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


def grow_time(choice):
    if choice == 3:
        for i in range(0, 80, 5):
            cd_pen.clear()
            cd_pen.write("3", align="center", font=("Courier", i, "bold"))
    elif choice == 2:
        for i in range(0, 80, 5):
            cd_pen.clear()
            cd_pen.write("2", align="center", font=("Courier", i, "bold"))
    else:
        for i in range(0, 80, 5):
            cd_pen.clear()
            cd_pen.write("1", align="center", font=("Courier", i, "bold"))


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    pen.goto(0, 260)
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Control
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Countdown
        win.update()
        grow_time(3)
        time.sleep(0.5)
        cd_pen.clear()
        grow_time(2)
        time.sleep(0.5)
        cd_pen.clear()
        grow_time(1)
        time.sleep(0.5)
        cd_pen.clear()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Countdown
        win.update()
        grow_time(3)
        time.sleep(0.5)
        cd_pen.clear()
        grow_time(2)
        time.sleep(0.5)
        cd_pen.clear()
        grow_time(1)
        time.sleep(0.5)
        cd_pen.clear()

    # Collisions
    if (335 < ball.xcor() < 350) and ((paddle_b.ycor() - 50) < ball.ycor() < (paddle_b.ycor() + 50)):
        ball.setx(335)
        ball.dx *= -1

    if (-335 > ball.xcor() > -350) and ((paddle_a.ycor() - 50) < ball.ycor() < (paddle_a.ycor() + 50)):
        ball.setx(-335)
        ball.dx *= -1
