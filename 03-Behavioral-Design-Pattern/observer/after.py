from enum import StrEnum, auto
from typing import Any, Callable


class Status(StrEnum):
    WAITING_FOR_PAYMENT = auto()
    PREPARING = auto()
    DISPATCHED = auto()
    DELIVERING = auto()
    DELIVERED = auto()


class Order:
    def __init__(self):
        self._status = Status.WAITING_FOR_PAYMENT
        self.callback = None

    def on_status_change(self, callback: Callable[[Status], Any]):
        self.callback = callback

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Status):
        if self._status != value and self.callback is not None:
            self.callback(value)
        self._status = value


def process_order():
    order = Order()
    order.on_status_change(lambda v: print(f"Status has changed to {v}"))
    order.status = Status.PREPARING


if __name__ == "__main__":
    process_order()
