from dataclasses import dataclass

from enum import Enum 
from typing import Any


class PaymentStatus(Enum):
    CANCELED = "canceled"
    PENDING = "pending"
    PAID = "paid"


class PaymentStatusError(Exception):
    pass 


@dataclass
class OrderNotEncapulationNoInformationHiding:
    ''' anyone can get the payment status directly via the instance variable '''
    payment_status: PaymentStatus = PaymentStatus.PENDING


@dataclass 
class OrderEncapsulatedNoInformationHiding:
    """"There is an interface now that you should use that provide encapsulation
    users of this class still need to know that the status is represented by an enum type"""

    _payment_status = PaymentStatus.PENDING 

    def get_payment_status(self):
        return self._payment_status


    def set_payment_status(self, status: PaymentStatus):
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentError(
                "you cant' change the status of an already paid order")
        self._payment_status = status


@dataclass 
class OrderEncapsulationAndInformationHiding:
    """ The status variable is set to `private`.  the only thing you're supposed to use
    is the is_paid method, you need no knowledge of how status is represented (that information 
    is hidden). """

    _payment_status: PaymentStatus = PaymentStatus.PENDING 


    def is_paid(self):
        return self._payment_status == PaymentStatus.PAID 

    def is_canceled(self):
        return self._payment_status == PaymentStatus.CANCELED

    def canceled(self):
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("You can't cancel an already paid order.")
        self._payment_status = PaymentStatus.CANCELED


    def pay(self):
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("Order already paid")
        self._payment_status = PaymentStatus.PAID 


@dataclass
class OrderInformationHidingWithoutEncapsulation:
    """The status variable is public again (so there's no boundary),
    but we don't know what the type is - that information is hidden. I know, it's a bit
    of a contrived example - you wouldn't ever do this. But at least it shows that
    it's possible."""

    payment_status: Any = None

    def is_paid(self) -> bool:
        return self.payment_status == PaymentStatus.PAID

    def is_cancelled(self) -> bool:
        return self.payment_status == PaymentStatus.CANCELLED

    def cancel(self) -> None:
        if self.payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("You can't cancel an already paid order.")
        self.payment_status = PaymentStatus.CANCELLED

    def pay(self) -> None:
        if self.payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("Order is already paid.")
        self.payment_status = PaymentStatus.PAID


def main() -> None:
    test = OrderInformationHidingWithoutEncapsulation()
    test.pay()
    print("Is paid: ", test.is_paid())


if __name__ == "__main__":
    main()



