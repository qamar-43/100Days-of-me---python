import turtle as t
import  random

jim = t.Turtle()


colours = ["blue", "medium violet red", "dark orange", "black","gold", "orange red", "lime", "rebecca purple", "steel blue", "dim gray"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        jim.forward(100)
        jim.right(angle)

for shape_side_n in range(3, 11):
    jim.color(random.choice(colours))
    draw_shape(shape_side_n)


