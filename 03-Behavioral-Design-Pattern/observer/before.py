from enum import StrEnum, auto


class Status(StrEnum):
    WAITING_FOR_PAYMENT = auto()
    PREPARING = auto()
    DISPATCHED = auto()
    DELIVERING = auto()
    DELIVERED = auto()


class Order:
    def __init__(self):
        self._status = Status.WAITING_FOR_PAYMENT

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Status):
        self._status = value


def process_order():
    order = Order()

    # This line would be repeated in many places over the code
    old_status = order.status
    order.status = Status.PREPARING
    if order.status != old_status:
        print(f"Status has changed to {order.status}")


if __name__ == "__main__":
    process_order()
