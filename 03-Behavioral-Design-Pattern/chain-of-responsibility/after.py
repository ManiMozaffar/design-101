import random
import string
from abc import ABC, abstractmethod
from typing import Type

from rich import print
from rich.traceback import install

install(show_locals=True)


# Exception classes remain unchanged
class AccessTokenInvalid(Exception):
    ...


class RefreshTokenInvalid(Exception):
    ...


class Auth0CodeInvalid(Exception):
    ...


def get_random_string(n: int):
    return "".join(random.choices(string.ascii_letters, k=n))


def api_call_failing_simulator():
    """Just a model to represent the probability of failure"""
    return random.choice([True, False])
    return True


# Handler abstract base class
class TokenHandler(ABC):
    name: str
    exc: Type[Exception]

    def __init__(self):
        self.next_handler = None
        self.last_handlers: list["TokenHandler"] = []
        self.final_token = None

    def set_next(self, handler: "TokenHandler"):
        self.next_handler = handler
        self.last_handlers = handler.last_handlers
        self.last_handlers.append(self)

    def handle(self) -> str | None:
        try:
            code = self.get_token()
            print(f"Fetched {self.name} = {code}")
            return code

        except self.exc:
            print(f"{self.name} invalid.")
            if self.next_handler:
                print(f"Trying {self.next_handler.name} handler now")
                current_code = self.next_handler.handle()
                if current_code:
                    return self.use_previous_fallbacks(current_code)

        return None

    @abstractmethod
    def get_token(self, token: None | str = None) -> str:
        "Implement this method to retrieve a token from the API endpoint"

    def use_previous_fallbacks(self, current_token: str) -> str:
        """Return all tokens in the loop"""
        print("Using previous handlers to retrieve first tokens")
        for handlers in self.last_handlers:
            if handlers.final_token:
                return handlers.final_token

        for handlers in self.last_handlers:
            current_token = handlers.get_token(current_token)

        self.final_result = current_token
        return self.final_result


class AccessTokenHandler(TokenHandler):
    name = "Access token"
    exc = AccessTokenInvalid

    def get_token(self, token: None | str = None) -> str:
        if token is None and api_call_failing_simulator() is True:
            raise self.exc()
        code = get_random_string(16)
        return code


class RefreshTokenHandler(TokenHandler):
    name = "Refresh token"
    exc = RefreshTokenInvalid

    def get_token(self, token: None | str = None) -> str:
        if token is None and api_call_failing_simulator() is True:
            raise self.exc()
        code = get_random_string(16)
        return code


class Auth0CodeHandler(TokenHandler):
    name = "Auth0 Code"
    exc = Auth0CodeInvalid

    def get_token(self, token=None) -> str:
        if api_call_failing_simulator() is True:
            raise self.exc()
        code = get_random_string(16)
        return code


if __name__ == "__main__":
    access_token_handler = AccessTokenHandler()
    refresh_token_handler = RefreshTokenHandler()
    auth0_code_handler = Auth0CodeHandler()
    access_token_handler.set_next(refresh_token_handler)
    refresh_token_handler.set_next(auth0_code_handler)

    token = access_token_handler.handle()
    print(f"Token obtained: {token}")
