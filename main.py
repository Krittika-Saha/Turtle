from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape('turtle')
colors = ['#b088f9', '#bedcfa', '#da9ff9', '#98acf8', '#d35d6e', '#ff8e71', '#fca3cc','#9088d4','#52057b','#006a71','#fcdada','#41aea9','#0d7377']

for i in range(3, 10):
  for j in range(i):
    timmy_the_turtle.fd(50)
    timmy_the_turtle.left(360/i)
    timmy_the_turtle.color(random.choice(colors))



screen = Screen()
screen.exitonclick()
