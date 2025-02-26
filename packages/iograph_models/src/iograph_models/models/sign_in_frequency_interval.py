from __future__ import annotations
from enum import Enum


class SignInFrequencyInterval(Enum):
	timeBased = "timeBased"
	everyTime = "everyTime"
	unknownFutureValue = "unknownFutureValue"

