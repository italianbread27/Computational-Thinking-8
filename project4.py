import turtle, time, random
from utils import *

# Section 1 - setup
set_background("spring")

prosciutto = 0
chickenparm = 0
cost = 30


# The goal of the game is to get as much prosciutto as possible and chicken parm


# Section 2 - controls
# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# Pressing "p" makes you one prosciutto

def get_prosciutto():
    global prosciutto
    prosciutto += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("prosciutto",x, y)

window.onkeypress(get_prosciutto, "p")

#Pressing "c" gets you chicken parm. Each chicken parm cost 30 prosciutto

def get_chickenparm():
    global prosciutto, chickenparm, cost
    if prosciutto >= cost:
        cost = cost * 2
        chickenparm += 1
        x = -400 + 120*chickenparm
        y = -250
        create_sprite("chickenparm.gif",x,y)

window.onkeypress(get_chickenparm, "c")


# Section 3 - game loop
window.listen()
for i in range(1000000000):
   
    # TODO - put any automatic actions here
 
    prosciutto += chickenparm


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()