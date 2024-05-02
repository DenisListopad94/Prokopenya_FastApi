from enum import Enum


class PaymentStatus(Enum):
    awaiting_execution = "awaiting_execution"
    confirmed = "confirmed"
    canceled = "canceled"

