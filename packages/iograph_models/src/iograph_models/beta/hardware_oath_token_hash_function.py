from __future__ import annotations
from enum import StrEnum


class HardwareOathTokenHashFunction(StrEnum):
	hmacsha1 = "hmacsha1"
	hmacsha256 = "hmacsha256"
	unknownFutureValue = "unknownFutureValue"

