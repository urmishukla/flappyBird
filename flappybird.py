import turtle
import time

wn= turtle.Screen()
wn.title("Flappy Bird by @urmishukla")
wn.bgcolor("deepskyblue")
wn.setup(width=500,height=800)
wn.tracer(0)

wn.register_shape("smallBirdGif.gif")

player=turtle.Turtle()

player.speed(0)
player.penup()
player.color("gold")
player.shape("smallBirdGif.gif")
player.goto(-200,0)
player.dx=0
player.dy=1

pipe1_top= turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("forestgreen")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid =18, stretch_len = 3, outline =None)
pipe1_top.goto (0,250)
pipe1_top.dx = -2
pipe1_top.dy= 0

pipe1_bottom= turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("forestgreen")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid =18, stretch_len = 3, outline =None)
pipe1_bottom.goto (0,-250)
pipe1_bottom.dx = -2
pipe1_bottom.dy= 0




gravity = -0.25

def goUp():
    player.dy += 7.5

wn.listen()
wn.onkeypress(goUp, "space")
    

#main game loop
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
    
    #move pipes
    x= pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x)
    
    x= pipe1_bottom.xcor()
    x += pipe1_bottom.dx
    pipe1_bottom.setx(x)



    
wn.mainloop()
