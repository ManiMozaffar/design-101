import random
import string

from rich import print
from rich.traceback import install

install(show_locals=True)


class AccessTokenInvalid(Exception):
    ...


class RefreshTokenInvalid(Exception):
    ...


class Auth0CodeInvalid(Exception):
    ...


class UnrecoverableState(Exception):
    ...


def get_random_string(n: int):
    return "".join(random.choices(string.ascii_letters, k=n))


def api_call_failing_simulator():
    """Just a model to represent the probability of failure"""
    # return random.choice([True, False])
    return True


def get_access_token(refresh_token: None | str = None) -> str:
    if refresh_token is None and api_call_failing_simulator() is True:
        raise AccessTokenInvalid()
    code = get_random_string(16)
    print(f"Fetched access token {code}")
    return code


def get_refresh_token(auth0_code: None | str = None) -> str:
    if auth0_code is None and api_call_failing_simulator() is True:
        raise RefreshTokenInvalid()
    code = get_random_string(16)
    print(f"Fetched Refresh token {code}")
    return code


def login_again() -> str:
    if api_call_failing_simulator() is True:
        raise Auth0CodeInvalid()
    code = get_random_string(16)
    print(f"Fetched Auth0 code {code}")
    return code


def access_token_flow():
    access_token_in_db = None  # assumes token is already gone from database or expired

    try:
        return get_access_token(access_token_in_db)
    except AccessTokenInvalid:
        print("First fallback failed. Trying refresh token now")
        try:
            refresh_token = get_refresh_token()
            access_token = get_access_token(refresh_token)
            return access_token
        except RefreshTokenInvalid:
            print("Second fallback failed. Trying auth0 now")

            try:
                auth_0_code = login_again()
                refresh_token = get_refresh_token(auth_0_code)
                access_token = get_access_token(refresh_token)
                return access_token
            except Auth0CodeInvalid:
                raise UnrecoverableState(
                    "Invalid access/refresh/auth0 token. User should be authenticated again"
                )


if __name__ == "__main__":
    access_token_flow()
