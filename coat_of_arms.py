# Section 1 - Your code
from utils import *
set_background("images")

s1 = create_sprite("cardinal",150, 100)
s2 = create_sprite("skier", -100, 100)
s3 = create_sprite("dog", -100, -100)
s4 = create_sprite("bike", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Conrad",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("a river cuts through rock,not because of its power, because of persistance",font = ("Arial", 5, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()