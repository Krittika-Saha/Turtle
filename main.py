from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape('turtle')
colors = ['#b088f9', '#bedcfa', '#da9ff9', '#98acf8', '#d35d6e', '#ff8e71', '#fca3cc','#9088d4','#52057b','#006a71','#fcdada','#41aea9','#0d7377']
directions = [0, 90, 180, 270]

timmy.pensize(10)
for i in range(200):
  timmy.fd(50)
  timmy.setheading(random.choice(directions))
  timmy.color(random.choice(colors))



screen = Screen()
screen.exitonclick()
