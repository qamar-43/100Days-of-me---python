import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Turtle Keyboard Drawing")
t = turtle.Turtle()
t.speed("fast")

# Make sure pen is down to draw
t.pendown()

# Movement functions
def move_forward():
    t.forward(50)

def move_backward():
    t.backward(50)

def turn_right():
    t.right(45)

def turn_left():
    t.left(45)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# Set up key bindings
screen.listen()              # Start listening for key presses
screen.onkey(move_forward, "f")   # lowercase 'f'
screen.onkey(move_backward, "b")
screen.onkey(turn_right, "r")
screen.onkey(turn_left, "l")
screen.onkey(clear_screen, "c")

# Keep the window open
screen.mainloop()



# this is coe snippet to draw anything in turtle by pressing keys like in ms_word paint
