from abc import ABC, abstractmethod


# Abstract Product Classes
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class TextField(ABC):
    @abstractmethod
    def render(self):
        pass


# Concrete Product Classes for Light Theme
class LightButton(Button):
    def render(self):
        return "Light Theme Button"


class LightTextField(TextField):
    def render(self):
        return "Light Theme TextField"


# Concrete Product Classes for Dark Theme
class DarkButton(Button):
    def render(self):
        return "Dark Theme Button"


class DarkTextField(TextField):
    def render(self):
        return "Dark Theme TextField"


# Abstract Factory Class
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        pass


# Concrete Factory for Light Theme
class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_text_field(self):
        return LightTextField()


# Concrete Factory for Dark Theme
class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_text_field(self):
        return DarkTextField()


# Client code
def ui_elements_factory(factory: UIFactory):
    button = factory.create_button()
    text_field = factory.create_text_field()

    print(button.render())
    print(text_field.render())


if __name__ == "__main__":
    # Usage
    print("Light Theme UI:")
    ui_elements_factory(LightThemeFactory())

    print("\nDark Theme UI:")
    ui_elements_factory(DarkThemeFactory())
