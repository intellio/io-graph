from __future__ import annotations
from enum import Enum


class BookingPriceType(Enum):
	undefined = "undefined"
	fixedPrice = "fixedPrice"
	startingAt = "startingAt"
	hourly = "hourly"
	free = "free"
	priceVaries = "priceVaries"
	callUs = "callUs"
	notSet = "notSet"
	unknownFutureValue = "unknownFutureValue"

