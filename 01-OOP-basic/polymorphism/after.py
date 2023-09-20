class Vehicle:
    def move(self):
        raise NotImplementedError


class Car(Vehicle):
    def move(self):
        return "Vroom!"


class Boat(Vehicle):
    def move(self):
        return "Splash!"


vehicles: list[Vehicle] = [Car(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
