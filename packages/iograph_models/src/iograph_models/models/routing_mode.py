from __future__ import annotations
from enum import StrEnum


class RoutingMode(StrEnum):
	oneToOne = "oneToOne"
	multicast = "multicast"
	unknownFutureValue = "unknownFutureValue"

