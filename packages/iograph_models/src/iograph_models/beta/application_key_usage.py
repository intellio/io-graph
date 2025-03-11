from __future__ import annotations
from enum import StrEnum


class ApplicationKeyUsage(StrEnum):
	sign = "sign"
	verify = "verify"
	unknownFutureValue = "unknownFutureValue"

