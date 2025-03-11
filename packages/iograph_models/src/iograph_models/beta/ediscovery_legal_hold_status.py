from __future__ import annotations
from enum import StrEnum


class EdiscoveryLegalHoldStatus(StrEnum):
	Pending = "Pending"
	Error = "Error"
	Success = "Success"
	UnknownFutureValue = "UnknownFutureValue"

