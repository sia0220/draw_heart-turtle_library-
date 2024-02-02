import time #Add time library
import turtle #Add turtle library

turtle.bgcolor("yellow") # 'bgcolor' is for background color
turtle.hideturtle() # this method add a hide Atribut to your program
t = turtle.Turtle() # Add a variable that is the name of your turtle
turtle.speed(1) # you can give a speed Atribut
t.hideturtle() # this method hide your turtle arrow , so you won't see the turtle

t.color("blue") # the color of your turtle
t.pensize(10) # changing the thickness of the path that the turtle leaves behind
t.begin_fill() # this method start fill the shape that your turtle made
t.fillcolor("red") # the color of your shape

t.left(140) # specifies the direction of rotation based on degrees
t.forward(177) # move the turtle forward 

t.circle(-90, 200) # we use the circle method to made the heart
t.setheading(60) #sets the orientation of the turtle to angle , based on degrees
# The First half of the heart↑
t.circle(-90, 200)
t.forward(177)
# The second half of the heart↑
t.end_fill() # this method end fill the shape that your turtle made

# Note : 'begin_fill/end_fill' any shape between these methodes will be fill↑

t.penup() #picks up the turtles tail so that it doesn't draw when it moves
t.left(60) 
t.forward(100)
# Note : Specify the location of the text↑
t.write("Sia-0220 ", 'false', 'center', font=('Showcard gothic', 60))
# Note: write the text at the center of the page with the specific font and size↑

time.sleep(3) # the amount of time that the program screen will be displayed after the program ends.
