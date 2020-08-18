import time
import turtle
from gfactor import gfactor, v
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1200,height=600)
wn.title("Simple anolog clock by using turtle modue using python in windows.")
wn.tracer(0)
h=0
m=0
s=0
ho=0
mo=0
so=0
#Creating our drawing pen
pen=turtle.Turtle()
pen.speed(0)
pen.pensize(10)
from datetime import datetime

def draw_clock1( h, m, s, pen):
    #Draw the clock face
    pen.penup()
    pen.goto(-300,210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)


    #Draw the lines for the hours
    pen.penup()
    pen.goto(-300,0)
    pen.setheading(90)
    pen.hideturtle()


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(-300,0)
        pen.rt(30)

    # Draw,the hour hand
    pen.penup()
    pen.goto(-300,0)
    pen.color("white")
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw,the minute hand
    pen.penup()
    pen.goto(-300,0)
    pen.color("white")
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    # Draw,the second hand:
    pen.penup()
    pen.goto(-300,0)
    pen.color("white")
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(179)
    pen.penup()

    #Title
    pen.color("white")
    pen.penup()
    pen.goto(-300,-275)
    pen.pendown()
    pen.write("Actual Time",False,"center",font=("Roboto",24,"bold"))#Actial Time Title

    #Digital
    pen.penup()
    pen.goto(-300,220)
    pen.pendown()
    pen.write(( f"{'{0:0=2d}'.format(h)} : {'{0:0=2d}'.format(m)} : {'{0:0=2d}'.format(s)}"),False,"center",font=("Roboto",24,"bold"))#Actial Digital Clock
    pen.penup()
    pen.goto(-300,260)
    pen.pendown()
    pen.write("H        M        S",False,"center",font=("Roboto",16,"bold"))

def draw_clock2( ho, mo, so, pen):
    #Draw the clock face
    pen.penup()
    pen.goto(300,210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)


    #Draw the lines for the hours
    pen.penup()
    pen.goto(300,0)
    pen.setheading(90)
    pen.hideturtle()


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(300,0)
        pen.rt(30)

    # Draw,the hour hand
    pen.penup()
    pen.goto(300,0)
    pen.color("white")
    pen.setheading(90)
    angle=(ho/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw,the minute hand
    pen.penup()
    pen.goto(300,0)
    pen.color("white")
    pen.setheading(90)
    angle=(mo/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    # Draw,the second hand:
    pen.penup()
    pen.goto(300,0)
    pen.color("white")
    pen.setheading(90)
    angle=(so/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(179)
    pen.penup()

    #Title
    pen.penup()
    pen.goto(300,-275)
    pen.pendown()
    pen.write("Relative Time",False,"center",font=("Roboto",24,"bold"))#Relative Time Title

    #Digital
    pen.penup()
    pen.goto(170,220)
    pen.pendown()
    pen.write(( f"{'{0:0=2d}'.format(ho)} : {'{0:0=2d}'.format(mo)} : {'{0:0=2d}'.format(int(so))} : {int(100*(so-int(so)))}"),False,"left",font=("Roboto",24,"bold"))#Relative Digital Clock
    pen.penup()
    pen.goto(185,260)
    pen.pendown()
    pen.write("H        M        S      MS",False,"left",font=("Roboto",16,"bold"))

while True:
    if s<60:
        s+=1
        if s==60:
            s=0
            m+=1
            if m==60:
                h+=1
                m=0
                if h==12:
                    h=0
    if so<60:
        so+=(1/gfactor)
        if so>=60:
            so=0
            mo+=1
            if mo==60:
                ho+=1
                mo=0
                if ho==12:
                    ho=0

    draw_clock1( h, m, s, pen)
    draw_clock2( ho, mo, so, pen)

    wn.update()
    time.sleep(1)

    pen.clear()

wn.mainloop()
