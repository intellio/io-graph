from __future__ import annotations
from enum import StrEnum


class DestinationType(StrEnum):
	new = "new"
	inPlace = "inPlace"
	unknownFutureValue = "unknownFutureValue"

