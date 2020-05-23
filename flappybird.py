import turtle
import time
import random

wn= turtle.Screen()
wn.title("Flappy Bird by @urmishukla")
#wn.bgcolor("deepskyblue")
wn.setup(width=500,height=800)
wn.bgpic("bgFadedFinalGIF.gif")
wn.tracer(0)

wn.register_shape("smallBirdGif.gif")
wn.register_shape("3x30Pipe.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Helvetica", 32, "normal"))


player=turtle.Turtle()

player.speed(0)
player.penup()
player.color("gold")
player.shape("smallBirdGif.gif")
player.goto(-200,0)
player.dx=0
player.dy=1


class pipes:
    limit = random.randint(0, 500)
    pipe_top= turtle.Turtle()
    pipe_top.speed(0)
    pipe_top.penup()
    #pipe_top.color("blue")
    pipe_top.shape("3x30Pipe.gif")
    pipe_top.shapesize(stretch_wid =30, stretch_len = 3, outline =None)
    pipe_top.goto (200, (250+limit))
    pipe_top.dx = -2
    pipe_top.dy= 0
    pipe_top.value=1

    pipe_bottom= turtle.Turtle()
    pipe_bottom.speed(0)
    pipe_bottom.penup()
    #pipe_bottom.color("forestgreen")
    pipe_bottom.shape("3x30Pipe.gif")
    pipe_bottom.shapesize(stretch_wid =30, stretch_len = 3, outline =None)
    pipe_bottom.goto (200, (limit-500))
    pipe_bottom.dx = -2
    pipe_bottom.dy= 0
  

gravity = -0.4

def goUp():
    player.dy += 8

wn.listen()
wn.onkeypress(goUp, "space")

p1=pipes()

#main game loop
roundsWon=0
while True:
    #pause
    time.sleep(0.02)
    #update screen
    wn.update()
    
    #Move player
    player.dy += gravity
    y = player.ycor()
    y += player.dy
    player.sety(y)
    #if player.ycor() < -380:
        #player.dy = 0
        #player.sety(-390)
    
    #move pipes
    x= p1.pipe_top.xcor()
    x += p1.pipe_top.dx
    p1.pipe_top.setx(x)
    
    x= p1.pipe_bottom.xcor()
    x += p1.pipe_bottom.dx
    p1.pipe_bottom.setx(x)
    
    if ((-180.0 == p1.pipe_top.xcor() -30.0 or -180.0 == p1.pipe_top.xcor() or -180.0 == p1.pipe_top.xcor() +30.0 )and player.ycor()+20.0 >= p1.pipe_top.ycor() -300.0):
        #print((p1.pipe_top.xcor()), (p1.pipe_top.ycor()-225), player.ycor())
        wn.bye()
    elif  ((-180.0 == p1.pipe_bottom.xcor() -30.0 or -180.0 == p1.pipe_bottom.xcor() or -180.0 == p1.pipe_bottom.xcor() +30.0 ) and player.ycor() -20 <= p1.pipe_bottom.ycor()+300.0):
        #print((p1.pipe_top.xcor()), (p1.pipe_top.ycor()-225), player.ycor())
        wn.bye()
    elif (-180.0 == p1.pipe_top.xcor()+30.0):
        roundsWon+=1
        print ("Rounds Won: " + str(roundsWon))
        pen.clear()
        pen.hideturtle()
        pen.write(roundsWon, move=False, align="left", font=("Helvetica", 32, "normal"))
        
    if p1.pipe_top.xcor() < -300:
        limit = random.randint(0, 350)
        p1.pipe_top.setx(200)
        p1.pipe_top.sety(300+limit)
        p1.pipe_bottom.setx(200)
        p1.pipe_bottom.sety(limit-500)
    


    
wn.mainloop()

