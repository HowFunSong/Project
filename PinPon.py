#PinPon
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Shawnfu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#記分板Score

score_a = 0
score_b = 0

#建立物件
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#Pen 計分
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font =("Courier",24, "bold"))


#Funtion
#控制球拍
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)




#Keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#Main game loop #建立一個視窗，需要一直保持視窗存在，在建立完物件後啟動
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx) 
    ball.sety(ball.ycor()+ball.dy) 

    #Border checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1    
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font =("Courier",24, "bold"))

    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font =("Courier",24, "bold"))
    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dx *= -1
        
    
    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dx *= -1



