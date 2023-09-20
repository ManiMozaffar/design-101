from typing import Any


class Car:
    def drive(self):
        return "Vroom!"


class Boat:
    def sail(self):
        return "Splash!"


def move(obj: Any):
    if isinstance(obj, Car):
        obj.drive()
    elif isinstance(obj, Boat):
        obj.sail()


my_car = Car()
my_boat = Boat()

# Explicitly execute each method
print("Car:", move(Car()))
print("Boat:", move(Boat()))
