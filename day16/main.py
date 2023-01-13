from turtle import Turtle, Screen

#import Turtle module/class, to construct from blueprint
#construct new object
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("CadetBlue")
timmy.forward(200)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

