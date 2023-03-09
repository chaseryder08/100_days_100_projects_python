import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, Road

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
road = Road()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()


    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
    
    # detect success cross        
    if player.is_at_finish():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level_up()
            
            
screen.exitonclick()