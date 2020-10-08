# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:12:46 2020

@author: alaar_000
"""

import turtle
import random
from playsound import playsound

score=0
lives=10


main_window=turtle.Screen()
main_window.title("Falling Heart")
main_window.setup(width=600,height=800)
main_window.bgpic('back.gif')
main_window.tracer(0)
main_window.register_shape('redheart.gif')
main_window.register_shape('blackheart.gif')
main_window.register_shape('left.gif')
main_window.register_shape('right.gif')



pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('purple')
font=('courier',26,'bold')
pen.goto(0,260)
pen.write('score: {} --  lives: {} ' .format(score,lives), align='center',font=font)



direction='stop'


actor=turtle.Turtle()
actor.shape('right.gif')
actor.speed()
actor.penup()
actor.goto(0,-270)


red_hearts=[]

for i in range(10):
    red_heart=turtle.Turtle()
    red_heart.shape('redheart.gif')
    red_heart.speed(random.randint (1,4) )
    red_heart.penup()
    red_heart.goto(-50,270)
    red_hearts.append(red_heart)

black_hearts=[]

for i in range(10):
    black_heart=turtle.Turtle()
    black_heart.shape('blackheart.gif')
    black_heart.speed(random.randint (1,5) )
    black_heart.penup()
    black_heart.goto(-50,270)
    black_hearts.append(black_heart)


def move_left():
    global direction
    direction='left'
def move_right():
    global direction
    direction='right'
def stop_actor():
    global direction
    direction='stop'


main_window.listen()
main_window.onkeypress(move_left,'Left')
main_window.onkeypress(move_right,'Right')
main_window.onkeypress(stop_actor,'Down')





while True:
    main_window.update()
    if direction == 'left' :
        actor.shape('left.gif')
        x=actor.xcor()
        x -=.6
        if x < -270:
            x=270
        actor.setx(x)
        
    if direction=='right':
        actor.shape('right.gif')
        x=actor.xcor()
        x +=0.6
        if x > 270:
            x=270
        actor.setx(x)
        
        
        
    for red_heart in red_hearts:
        y=red_heart.ycor()
        y -=0.3*red_heart.speed()
        red_heart.sety(y)
        
        
        if y <-300:
            playsound('red.wav',False)
            x=random.randint(-270, 270)
            red_heart.goto(x,270)
    
        if red_heart.distance(actor)<20:
            x=random.randint(-270, 270)
            red_heart.goto(x,270)
            score+=10
            pen.clear()
            pen.write('score: {} --  lives: {} ' .format(score,lives), align='center',font=font)

           
            
    for black_heart in black_hearts:
        y=black_heart.ycor()
        y -=0.3*black_heart.speed()
        black_heart.sety(y)
        
        
        if y <-300:
            x=random.randint(-270, 270)
            black_heart.goto(x,270)
    
        if black_heart.distance(actor)<20:
                playsound('black.wav',False)
                x=random.randint(-270, 270)
                black_heart.goto(x,270)
                score-=10
                lives-=1
                if lives <0:
                    main_window.bye()
                    exit(0)
                pen.clear()
                pen.write('score: {} --  lives: {} ' .format(score,lives), align='center',font=font)

    















main_window.mainloop()























