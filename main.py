import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color_tuple = (r, g, b)
  return color_tuple

timmy.shape('classic')
colors = ['#b088f9', '#bedcfa', '#da9ff9', '#98acf8', '#d35d6e', '#ff8e71', '#fca3cc','#9088d4','#52057b','#006a71','#fcdada','#41aea9','#0d7377']
directions = [0, 90, 180, 270]

timmy.speed('fastest')
def draw_circle(gap_size):
  for i in range(360//gap_size):
    timmy.circle(100)
    timmy.setheading(gap_size)
    gap_size += 5
    timmy.color(random.choice(colors))

draw_circle(5)



screen = t.Screen()
screen.exitonclick()
