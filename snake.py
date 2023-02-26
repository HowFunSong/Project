import turtle
import time
import random

delay = 0.1


#score
score = 0
high_score = 0




#Set up the screen
wn = turtle.Screen()
wn.title = ("Snake Game by @Eric")
wn.bgcolor("black")
wn.setup(width= 600,height = 800)
wn.tracer(0) #turns off the screen update

#Snake head 建立貪食蛇的物件
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segaments = []

#Pen 
pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Scroe: 0 High Score: 0", align = "center", font=("Calibri", 24, "normal","bold") )


#functions 控制函式
#control function
def go_up():
    if head.direction != "down" :
        head.direction ="up"
def go_down():
    if head.direction != "up" :
        head.direction ="down"
def go_right():
    if head.direction != "left" :
        head.direction ="right"
def go_left():
    if head.direction != "right" :
        head.direction ="left"



def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety( y + 20)

    if head.direction == "down" :
        y = head.ycor()
        head.sety( y - 20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx( x + 20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx( x - 20)


#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")


#Main game loop
while True:    
    wn.update()

    # Check for collision with the border 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>390 or head.ycor()<-390:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #hide the segament
        for segment in segaments:
            segment.goto(1000,1000)

        #Clear the segament list
        segaments.clear()
        
        #reset the delay
        delay = 0.1    
        
        score = 0
        pen.clear()
        pen.write(f"Scroe: {score} High Score: {high_score}", align = "center", font=("Calibri", 24, "normal","bold") )

    # Check for collision with the body it self
    for segment in segaments:
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segament
            for segment in segaments:
                segment.goto(1000,1000)

            #Clear the segament list
            segaments.clear()

            #reset score
            score = 0

            #reset the delay
            delay = 0.1    

            #update the score
            pen.clear()
            pen.write(f"Scroe: {score} High Score: {high_score}", align = "center", font=("Calibri", 24, "normal","bold") )

    if head.distance(food) < 20:
        
        #Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-390,390)
        food.goto(x,y)

        #add a segatment 
        new_segament = turtle.Turtle()
        new_segament.speed(0)
        new_segament.shape("square")
        new_segament.color("grey")
        new_segament.penup()
        segaments.append(new_segament)
        #Shorten the delay 
        delay -= 0.001

        #increase the score 
        score += 10
        if score > high_score :
            high_score = score

        pen.clear()
        pen.write(f"Scroe: {score} High Score: {high_score}", align = "center", font=("Calibri", 24, "normal","bold") )
    
    #Move the end segament first in reverse order 但是當index = 0 直接停止，所以需要再增加個函式 
    for index in range(len(segaments)-1, 0, -1):
        x = segaments[index-1].xcor()
        y = segaments[index-1].ycor()
        segaments[index].goto(x,y) 
    
    #Move segament 0 to where the head is 
    if len(segaments) > 0 :
        x = head.xcor()
        y = head.ycor()
        segaments[0].goto(x,y)


    move()
  
    time.sleep(delay)








wn.mainloop()
