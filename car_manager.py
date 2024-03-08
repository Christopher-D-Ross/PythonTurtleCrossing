import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# This class will generate the random cars and move them across the screen.
class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = 0

    def create_car(self):
        # Instituting a 1 in 6 chance a car will get created each time the method is called.
        # The purpose of the 1 in 6 chance is to slow down the creation of cars.
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-250, 250))
            self.all_cars.append(new_car)

    def move_all_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
