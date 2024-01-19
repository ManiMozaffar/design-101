from enum import StrEnum, auto
from typing import Any, Callable


class Status(StrEnum):
    WAITING_FOR_PAYMENT = auto()
    PAID = auto()
    PREPARING = auto()
    DISPATCHED = auto()
    DELIVERING = auto()
    DELIVERED = auto()


class Order:
    def __init__(self):
        self._status = Status.WAITING_FOR_PAYMENT
        self.callbacks: list[Callable[[Status], Any]] = []

    def on_status_change(self, callback: Callable[[Status], Any]):
        self.callbacks.append(callback)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Status):
        if self._status != value:
            for callback in self.callbacks:
                callback(value)

        self._status = value


def process_order():
    order = Order()
    order.on_status_change(lambda v: print(f"[EMAIL] Status has changed to {v}"))
    order.on_status_change(lambda v: print(f"[NOTIFICATION] Status has changed to {v}"))

    order.on_status_change(
        lambda v: print("[SUPPORT TICKET] Order is paid, please deliver the order")
        if v is Status.PAID
        else ...
    )
    order.status = Status.PREPARING
    order.status = Status.PREPARING
    order.status = Status.PREPARING
    order.status = Status.PREPARING
    order.status = Status.PREPARING
    order.status = Status.PAID
    order.status = Status.DISPATCHED
    order.status = Status.DELIVERING
    order.status = Status.DELIVERED


if __name__ == "__main__":
    process_order()
