# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:31:21 2021

@author: Admin
"""

from turtle import Turtle, Screen
oyna= Screen()
oyna.title('ollit ')

chiziq = Turtle()
chiziq.color('red')
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300,300)
chiziq.down()
chiziq.goto(300,-300)
chiziq.goto(-300,-300)
chiziq.goto(-300,300)
chiziq.goto(300,300)
savat = Turtle()
savat.color('green')
savat.pensize(7)
savat.speed(0)
savat.hideturtle()
savat.up()
savat.goto(0,-300)
savat.down()
savat.goto(0,-250)
savat.goto(220,-250)
savat.goto(220,-300)
koptok = Turtle()
koptok.shape('circle')
koptok.color('green')
koptok.up()
koptok.goto(0,0)

step_x = 3
step_y = 2
while True:
 x, y =koptok.position()
 if x + step_x >=300 or x + step_x<= -300:
  step_x = -step_x
 if y + step_y >=300 or y + step_y <=-300:
  step_y = -step_y
  if x <=-0 and y == -250:
   break
 koptok.goto(x+step_x, y+step_y)

oyna.mainloop()