from random import choice, random
from turtle import *
from UtilitiesUsedForGames import vector

def Value():
    #This will randomly generate a value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

Ball_ = vector(0, 0)
Aim_ = vector(Value(), Value())
State_ = {1: 0, 2: 0}

def move(player, change):
    #This moves the  player position by change.
    State_[player] += change

def rectangle(X_Axis, Y_Axis, Width, Height):
    #Draws a rectangle at (X_Axis, Y_Axis) with given Width and Height.
    up()
    goto(X_Axis, Y_Axis)
    down()
    begin_fill()
    for count in range(2):
        forward(Width)
        left(90)
        forward(Height)
        left(90)
    end_fill()

def draw():
    #Draws the ping pong Ball_ for the game
    clear()
    rectangle(-200, State_[1], 10, 50)
    rectangle(190, State_[2], 10, 50)

    Ball_.move(Aim_)
    X_Axis = Ball_.X_Axis
    Y_Axis = Ball_.Y_Axis

    up()
    goto(X_Axis, Y_Axis)
    dot(10)
    update()

    if Y_Axis < -200 or Y_Axis > 200:
        Aim_.Y_Axis = -Aim_.Y_Axis

    if X_Axis < -185:
        low = State_[1]
        high = State_[1] + 50

        if low <= Y_Axis <= high:
            Aim_.X_Axis = -Aim_.X_Axis
        else:
            return

    if X_Axis > 185:
        low = State_[2]
        high = State_[2] + 50

        if low <= Y_Axis <= high:
            Aim_.X_Axis = -Aim_.X_Axis
        else:
            return

    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'a')
onkey(lambda: move(1, -20), 'z')
onkey(lambda: move(2, 20), 'k')
onkey(lambda: move(2, -20), 'm')
draw()
done()
