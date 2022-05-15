import turtle 

#Creating a window 
wn = turtle.Screen()
wn.title("Pong by @SiddheshwariThakur")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0) #Allows us to speed up the game

#Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)   #This sets the speed of animation to the maximum possible speed.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   #This sets the speed of animation to the maximum possible speed.
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

#Ball 
ball = turtle.Turtle()
ball.speed(0)   #This sets the speed of animation to the maximum possible speed.
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 #everytime the ball moves, it will move by 2 pixels. 
ball.dy = 0.1

#Pen 
pen = turtle.Turtle() 
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0       Player B: 0", align="center", font=("Helvetica", 16, "normal"))

#Score
score_a = 0
score_b = 0

#Functions 
def moveup_paddle_a(): 
    y = paddle_a.ycor() #This returns the y-coordinate of the paddle. 
    y += 20 #adds 20 pixels. 
    paddle_a.sety(y)
    
def movedown_paddle_a(): 
    y = paddle_a.ycor() #This returns the y-coordinate of the paddle. 
    y -= 20 #adds 20 pixels. 
    paddle_a.sety(y)
    
def moveup_paddle_b():
    y = paddle_b.ycor() #This returns the y-coordinate of the paddle. 
    y += 20 #adds 20 pixels. 
    paddle_b.sety(y)

def movedown_paddle_b():
    y = paddle_b.ycor() #This returns the y-coordinate of the paddle. 
    y -= 20 #adds 20 pixels. 
    paddle_b.sety(y)
    
#Keyboard binding 
wn.listen() #Listens for keyboard input.
wn.onkeypress(moveup_paddle_a, "w") #When the user presses w, we call moveup_paddle_a()
wn.onkeypress(movedown_paddle_a, "s")
wn.onkeypress(moveup_paddle_b, "i")
wn.onkeypress(movedown_paddle_b, "k")

#Every game needs a main game loop.
while True:
    wn.update() 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}       Player B: {}".format(score_a, score_b), align="center", font=("Helvetica", 16, "normal"))
    if ball.xcor() < -390:
        ball.setx(390)
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player A: {}       Player B: {}".format(score_a, score_b), align="center", font=("Helvetica", 16, "normal"))
        
    #Paddle and ball collision 
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40) and ball.xcor() < 350:
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40) and ball.xcor() > -350:
        ball.setx(-340)
        ball.dx *= -1
