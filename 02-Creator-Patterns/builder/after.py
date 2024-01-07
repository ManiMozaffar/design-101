from typing import Self


# Product
class Car:
    def __init__(self, engine: str, seats: int, gps: str | None = None):
        self.engine = engine
        self.seats = seats
        self.gps = gps

    def __str__(self):
        return f"Car with {self.engine} engine, {self.seats} seats, GPS: {self.gps}"


# Builder Interface
class CarBuilder:
    def set_engine(self, engine: str) -> Self:
        raise NotImplementedError

    def set_seats(self, seats: int) -> Self:
        raise NotImplementedError

    def set_gps(self, gps: str) -> Self:
        raise NotImplementedError

    def build(self) -> Car:
        raise NotImplementedError


# Concrete Builder
class ConcreteCarBuilder(CarBuilder):
    def __init__(self):
        self.engine = ""
        self.seats = 0
        self.gps = None

    def set_engine(self, engine: str):
        self.engine = engine
        return self

    def set_seats(self, seats: int):
        self.seats = seats
        return self

    def set_gps(self, gps: str):
        self.gps = gps
        return self

    def build(self) -> Car:
        return Car(self.engine, self.seats, self.gps)


# Director
class CarDirector:
    @staticmethod
    def construct_sports_car(builder: CarBuilder) -> Car:
        return builder.set_engine("V8").set_seats(2).set_gps("Sport GPS").build()

    @staticmethod
    def construct_family_car(builder: CarBuilder) -> Car:
        return builder.set_engine("V6").set_seats(5).build()
