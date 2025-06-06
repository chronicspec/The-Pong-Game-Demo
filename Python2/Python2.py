import turtle as t
playerAscore = 0
playerBscore = 0

#create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

#Creating the left paddle
leftPaddle=t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5,stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350,0)

#Creating the right paddle
rightPaddle=t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5,stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(-350,0)

#Code for creating the ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2
  
#Code for creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))
  
#code for moving the leftpaddle
def leftpaddleup():
    y=leftPaddle.ycor()
    y=y+90
    leftPaddle.sety(y)
  
def leftpaddledown():
    y=leftPaddle.ycor()
    y=y+90
    leftPaddle.sety(y)
  
#code for moving the rightpaddle
def rightpaddleup():
    y=rightPaddle.ycor()
    y=y+90
    rightPaddle.sety(y)
  
def rightpaddledown():
    y=t.rightpaddle.ycor()
    y=y+90
    rightPaddle.sety(y)
  
#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')
  
while True:
    window.update()
  
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballxdirection)
  
    #border set up
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1
          
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")
  
  
    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")
  
     # Handling the collisions with paddles.
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
