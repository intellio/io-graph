from __future__ import annotations
from enum import Enum


class RoutingMode(Enum):
	oneToOne = "oneToOne"
	multicast = "multicast"
	unknownFutureValue = "unknownFutureValue"

