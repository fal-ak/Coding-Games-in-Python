#Game 1  Of PYTHON
#It is my Apple Game
#Made by Turtle
import sys

import turtle as t


s=t.Screen()

t.speed(10)

s.bgcolor("grey")




t.shape("circle")





s.setup(width = 700, height = 500, startx = 200, starty = 50)


t.pencolor("black")


def draw_apple():
   
    t.fillcolor("red")


    t.width(10)
    t.begin_fill()

    t.left(160)
    t.circle(100, 100)

    t.circle(200, 60)
    t.circle(40, 90)

    t.circle(-40, 100)
    t.circle(40, 100)

    t.circle(200, 30)
    t.left(90)

    t.circle(-70, 150)
    t.left(120)
    t.circle(160, 55)


    t.end_fill()





def draw_leaf():
    t.fillcolor("green")
    

    t.begin_fill()
    t.circle(-100, 90)
    t.right(90)
    t.circle(-100, 90)
    t.end_fill()







t.up()

t.goto(0, 80)

t.down()


draw_apple()


t.right(110)

t.up()

t.forward(25)

t.down()

draw_leaf()




t.done()










