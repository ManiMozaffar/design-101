DATABASE = {}


class Pet:
    def __init__(self, name: str, gender: str, age: int, color: str):
        self.name = name
        self.gender = gender
        self.age = age
        self.color = color

    def breathe(self) -> str:
        return "Inhale, exhale."

    def sleep(self) -> str:
        return "Sleeping peacefully."

    def move(self) -> str:
        return "Moving around."

    def make_sound(self) -> str:
        raise NotImplementedError

    def record_sound(self):
        result = self.make_sound()
        DATABASE[self.name] = result


class Dog(Pet):
    def __init__(self, name: str, gender: str, age: int, color: str, owner: str):
        super(Dog, self).__init__(name, gender, age, color)
        self.owner = owner

    def make_sound(self) -> str:
        return "Woof"


class Cat(Pet):
    def make_sound(self) -> str:
        return "Meow"


sparky = Dog(name="Sparky", gender="Male", age=2, color="Brown", owner="Mani")
print(sparky.breathe())  # Output: "Inhale, exhale."
print(sparky.make_sound())  # Output: "Woof"

whiskers = Cat(name="Whiskers", gender="Female", age=3, color="White")
print(whiskers.sleep())  # Output: "Sleeping peacefully."
print(whiskers.make_sound())  # Output: "Meow"
