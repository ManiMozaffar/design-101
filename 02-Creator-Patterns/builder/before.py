class Car:
    def __init__(self, engine: str, seats: int, gps: str | None = None):
        self.engine = engine
        self.seats = seats
        self.gps = gps

    def __str__(self):
        return f"Car with {self.engine} engine, {self.seats} seats, GPS: {self.gps}"


sports_car = Car("V8", 2, "Sport GPS")
print(sports_car)

family_car = Car("V6", 5)
print(family_car)
