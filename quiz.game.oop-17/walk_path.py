import turtle as t
import  random


t.colormode(255)
jim = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


jim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)


draw_spirograph(6)

screen = t.Screen()
screen.exitonclick()