import turtle
import time

boxsize = 200
caught = False
score = 0

#functions that are called on keypresses
def up() :
    mouse.forward(10)
    checkbound()

def left ():
    mouse.left(45)

def right () :
        mouse.right(45)

def quitTurtles ():
    window.bye ()

#stop the mouse from leaving the square set by box size
def checkboud ():
    global boxsize
    if mouse.xcor () > boxsize :
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor () < -boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)

#set up screen
window = turtle.Screen ()
mouse = turtle.Turtle ()
cat = turtle.Turtle ()
mouse.penup ()
mouse.penup ()
mouse.goto (100,100)

#add key listeners
window.onkeypress (up, "Up")
window.onkeypress (left, "Left")
window.onkeypress (right, "Right")
window.onkeypress (quitTurtles, "Escape")

difficulty = window.numinput("Difficulty",
                             "Enter a difficulty from easy (1), for hard (5) ", minval=1, maxval=5)

window.listen()

        #main loop
        #noten how it changes with difficulty
while not caught :
            cat.setheading(cat.towards(mouse))
            cat.forward(8+difficulty)
            score = score + 1
            if cat.distance(mouse) < 5:
                            caught = True
                            time.sleep(0.2-(0.01*difficulty))
window.textinput("GAME OVER", "Well done. You scored:"+ str (score*difficulty))
window.bye()
