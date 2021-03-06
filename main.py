from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


# Create 8 turtles
# w = forwards, s = backwards, a = counter-clockwise, d = clockwise
# Turtle draw a curve
# c = clear drawing, the put the turtle back in the center
# https://docs.python.org/3/library/turtle.html#turtle.dot

def move_forwards():   # function no argument
    tim.forward(10)   # move forward 10 paces
def move_backwards():
    tim.move_backward(10)
def turn_left() :
    new_heading = tim.heading() +10     # Turn left at 10 degree each time
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10  # Turn right at 10 degree each time
    tim.setheading(new_heading)

def clear():
    tim.clear()   # clear screen after drawing
    tim.penup()   # clear all the old roads when the turtle is gone
    tim.home()   # the turtle go back home at (0,0)
    tim.pendown() # ready for next moving




screen.listen()
#screen.onkey(key ="space",fun = move_forwards())    #fun	a function with no arguments, key
# a string: key (e.g. “a”) or key-symbol (e.g. “space”)

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


screen.exitonclick()