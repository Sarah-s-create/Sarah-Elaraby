import turtle 

wind = turtle.Screen()
wind.title("ping pong game")
wind.bgcolor(" black ")
wind.setup(width = 800, height = 600)
wind.tracer(0)

madrap1 = turtle.Turtle()
madrap1.speed()
madrap1.color("blue")
madrap1.shape("Square")
madrap1.shapesize(stretch_wid = 5, stretch_lin = 1)
madrap1.penup()
madrap1.goto(-350, 0)

madrap2 = turtle.Turtle()
madrap2.speed()
madrap2.color("red")
madrap2.shape("Square")
madrap2.shapesize(stretch_wid = 5, stretch_lin = 1)
madrap2.penup()
madrap2.goto(350, 0)

ball = turtle.Turtle()
ball.speed()
ball.color("white")
ball.shape("Square")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = -2.5
score1 = 0; score2 = 0
score = turtle.Turtle 
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.written("player 1 : {} player 2 : {}").format(score1, score2), align ="center", font("Courier", 24, "normal")




def madrap1_up(): 
    y = madrap1.ycor()
    y += 20
    madrap1.sety(y)
    
def madrap1_down(): 
    y = madrap1.ycor()
    y -= 20
    madrap1.sety(y)
    
def madrap2_up(): 
    y = madrap2.ycor()
    y += 20
    madrap2.sety(y)    
def madrap2_down(): 
    y = madrap2.ycor()
    y -= 20
    madrap2.sety(y)    
    
wind.listen()
wind.onkeypress(madrap1_up, "w")
wind.onkeypress(madrap1_down, "s")
wind.onkeypress(madrap2_up, "o")
wind.onkeypress(madrap2_up, "k")


while true : 
    wind.update()
    # move the ball
    ball.setx(ball.xcor(), ball.dx)
    ball.sety(ball.ycor(), ball.dy)
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290 :
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1    
        score.clear()
        score.written("player 1 : {} player 2 : {}").format(score1, score2), align ="center", font("Courier", 24, "normal")
    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1           
        score.written("player 1 : {} player 2 : {}").format(score1, score2), align ="center", font("Courier", 24, "normal")
    if (ball.xcor() > 340 and ball.xcor < 350) and (ball.ycor < madrab2.ycor() + 40 and ball.ycor > madrab2.ycor())  
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor > -350) and (ball.ycor < madrab2.ycor() + 40 and ball.ycor > madrab2.ycor())  
        ball.setx(-340)
        ball.dx *= -1
                