from __future__ import annotations
from enum import StrEnum


class BookingInvoiceStatus(StrEnum):
	draft = "draft"
	reviewing = "reviewing"
	open = "open"
	canceled = "canceled"
	paid = "paid"
	corrective = "corrective"

