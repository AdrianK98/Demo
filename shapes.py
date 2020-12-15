import turtle 
  
pen = turtle.Turtle() 
pen.speed(0)

def drawRing(x,y):
    pen.up() 
    pen.goto(x, y) 
    pen.down() 
    pen.circle(100) 
    pen.up() 
    pen.goto(x, y+20) 
    pen.down() 
    pen.circle(80)


def drawHeart(x,y):
    pen.up() 
    pen.goto(x, y) 
    pen.down()
    pen.left(140)
    pen.forward(123)
    for i in range(230):
        pen.right(1) 
        pen.forward(1)
        i+=1 
    pen.left(180) 

    for i in range(230):
        pen.right(1) 
        pen.forward(1)
        i+=1 
    pen.forward(123)
    pen.setheading(0)

def drawStar(x,y,m):
    pen.up()
    pen.goto(x,y)
    pen.down()
    for i in range(5):
        pen.right(144)
        pen.forward(m)
        pen.left(72)
        pen.forward(m)
  
def drawCrescent(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.right(110)
    for i in range(220):
        pen.forward(1)
        pen.left(1)
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.setheading(300)
    for i in range(120):
        pen.forward(1.1)
        pen.left(1)
    pen.setheading(0)

def drawElipse(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.setheading(-135)
    for i in range(2):
        pen.circle(100,90) 
        pen.circle(100/2,90) 
