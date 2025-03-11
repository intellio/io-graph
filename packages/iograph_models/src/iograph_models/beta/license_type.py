from __future__ import annotations
from enum import StrEnum


class LicenseType(StrEnum):
	notPaid = "notPaid"
	paid = "paid"
	trial = "trial"
	unknownFutureValue = "unknownFutureValue"

