import turtle

def draw_square(some_turtle):
    for i in range(1,5):
         some_turtle.forward(100)
         some_turtle.right(90)
#def draw_tringle(ss_turtle):
    #for i in range(1,4):
       #ss_turtle.forward(100)
        #ss_turtle.right(120)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("green")
    brad.speed(6)
    for i in range(1,37):
         draw_square(brad)
         brad.right(10)
    ##create the turtle angii - draws a circle
    #angii = turtle.Turtle()
    #angii.shape("arrow")
    #angii.color("black")
    #angii.circle(100)
    ##create the turtle mady - draws a tringle
    #mady = turtle.Turtle()
    #mady.shape("arrow")
    #angii.color("yellow")
    #draw_tringle(mady)
    #window.exitonclick()
draw_art()
