from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your Bet",
    prompt="Choose which color turtle is going to win the race. Enter a color:"
)

# Corrected color list (no trailing spaces) and aligned with y_positions
colors = ["red", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50]  # Now matches 5 turtles

all_turtles = []

# Create turtles properly and add to list
for index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)  # This line is essential!

if user_bet:
    is_race_on = True

# Run the race
while is_race_on:
    for racer in all_turtles:
        racer.forward(random.randint(1, 10))

        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race!")
            break

# Keep window open until clicked
screen.exitonclick()
