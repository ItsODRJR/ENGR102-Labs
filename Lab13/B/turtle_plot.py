# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: OSCAR RODRIGUEZ (635007029)
# Section: ENGR102-551
# Assignment: Lab13B
# Date: 18/11/24

import turtle
import random

def draw_vertical_tally(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(random.randint(85,95))
    turtle.forward(random.randint(15,30))

def draw_diagonal_tally(x, y):
    turtle.penup()
    turtle.goto(x - 30, y + 20)
    turtle.pendown()
    turtle.setheading(random.randint(-40,-30))
    turtle.forward(random.randint(35,40))

def draw_tally_group(x, y):
    spacing = 10
    for i in range(4):
        draw_vertical_tally(x + i * spacing, y)
    draw_diagonal_tally(x + 3 * spacing, y)

def draw_tallies(num):
    x, y = -200, 0 
    for i in range(num // 5):
        draw_tally_group(x, y)
        x, y = position_next_group(x, y)
    remaining = num % 5
    for j in range(remaining):
        draw_vertical_tally(x + j * 10, y)

def position_next_group(x, y):
    x += 60
    if x > 200: 
        x = -200
        y -= 30
    return x, y

num_tallies = int(input("Enter the number of tallies to draw (up to 100): "))
turtle.speed(0)
draw_tallies(num_tallies)
turtle.done()