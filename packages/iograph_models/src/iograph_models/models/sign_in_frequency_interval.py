from __future__ import annotations
from enum import StrEnum


class SignInFrequencyInterval(StrEnum):
	timeBased = "timeBased"
	everyTime = "everyTime"
	unknownFutureValue = "unknownFutureValue"

