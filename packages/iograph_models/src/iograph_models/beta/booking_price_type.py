from __future__ import annotations
from enum import StrEnum


class BookingPriceType(StrEnum):
	undefined = "undefined"
	fixedPrice = "fixedPrice"
	startingAt = "startingAt"
	hourly = "hourly"
	free = "free"
	priceVaries = "priceVaries"
	callUs = "callUs"
	notSet = "notSet"

