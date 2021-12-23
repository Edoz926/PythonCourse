# Simple Pong for beginners
import os.path
import turtle
import winsound

# crea la window
wn = turtle.Screen()
wn.title("Pong by @Edoz") #title
wn.bgcolor("black") #background color

# Change the size of the window
wn.setup(width=800, height=600)
wn.tracer(0)
# stops the window from updating, only manually refresh
# needed to make things faster, without it, it will be much slower

score_a = 0
score_b = 0

# add paddle to the left and right
# Paddle A
paddle_a =turtle.Turtle()
paddle_a.speed(0) #max speed of the object
paddle_a.shape("square")
paddle_a.color("white")
# the basic shape is 20*20px
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # draw lines while moving (not necessary)
# Want to set a start point for my paddle
paddle_a.goto(-350,0)


# Paddle B
paddle_b =turtle.Turtle()
paddle_b.speed(0) #max speed of the object
paddle_b.shape("square")
paddle_b.color("white")
# the basic shape is 20*20px
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() #draw lines while moving (not necessary)
# Want to set a start point for my paddle
paddle_b.goto(350,0)

# ball
ball =turtle.Turtle()
ball.speed(0) #max speed of the object
ball.shape("circle")
ball.color("white")
# the basic shape is 20*20px
ball.penup() #draw lines while moving (not necessary)
# Want to set a start point for my paddle
ball.goto(0,0)
# ball movements
ball.dx = 0.25
ball.dy = 0.25

# Punteggio
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #non need to see it
pen.goto(0,260)
pen.write(f"PlayerA: {score_a}  PlayerB: {score_b}", align="center",font=("ComicSans",24,"normal"))

"""
Function of the game
"""

# Move paddle
def paddle_a_up():
    y = paddle_a.ycor() #returns y coord
    y += 20
    paddle_a.sety(y)

def paddle_a_dw():
    y = paddle_a.ycor()  # returns y coord
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #returns y coord
    y += 20
    paddle_b.sety(y)

def paddle_b_dw():
    y = paddle_b.ycor() #returns y coord
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_dw, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_dw, "Down")
# Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #compare y/x ball coordinate and bounce
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound(os.path.join(os.getcwd(),"87553076.mp3"),winsound.SND_ASYNC)
        #clear the screen
        pen.clear()
        pen.write(f"PlayerA: {score_a}  PlayerB: {score_b}", align="center", font=("ComicSans", 24, "normal"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound(os.path.join(os.getcwd(),"87553076.mp3"),winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"PlayerA: {score_a}  PlayerB: {score_b}", align="center", font=("ComicSans", 24, "normal"))

    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

