import turtle
bob=turtle.Turtle()
turtle. colormode(255)
turtle.bgcolor("black")
bob.speed(12)
bob.width(3)

bob.penup()
bob.goto(0,0)
bob.pendown()
for times in range(29):
    for c in ["red","blue","green","pink"]:
        bob.color(c)
        bob. circle(200-times*5)
        bob. right(160)

bob.penup()
bob.goto(-600,300)
bob.pendown()


for times in range(200):
    c= (0,255-times,255-times)
    bob. color (c)
    bob. forward(200-times)
    bob. right (160)

bob.penup()
bob.goto(700,380)
bob.pendown()

for times in range(200):
    c= (0,255-times,255-times)
    bob. color (c)
    bob. forward(200-times)
    bob. right (160)

bob.penup()
bob.goto(-630,-270)
bob.pendown()

for times in range(200):
    c= (0,255-times,255-times)
    bob. color (c)
    bob. forward(200-times)
    bob. right (160)

bob.penup()
bob.goto(620,-230)
bob.pendown()

for times in range(200):
    c= (0,255-times,255-times)
    bob. color (c)
    bob. forward(200-times)
    bob. right (160)

turtle.done()



