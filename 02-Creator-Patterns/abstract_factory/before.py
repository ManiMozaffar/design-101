from typing import Literal


class LightButton:
    def render(self):
        return "Light Theme Button"


class LightTextField:
    def render(self):
        return "Light Theme TextField"


class DarkButton:
    def render(self):
        return "Dark Theme Button"


class DarkTextField:
    def render(self):
        return "Dark Theme TextField"


# Client code directly instantiates specific classes
def create_ui_elements(theme: Literal["light", "dark"]):
    if theme == "light":
        button = LightButton()
        text_field = LightTextField()
    elif theme == "dark":
        button = DarkButton()
        text_field = DarkTextField()
    else:
        raise ValueError("Unknown theme")

    print(button.render())
    print(text_field.render())


if __name__ == "__main__":
    # Usage
    print("Light Theme UI:")
    create_ui_elements("light")

    print("\nDark Theme UI:")
    create_ui_elements("dark")
