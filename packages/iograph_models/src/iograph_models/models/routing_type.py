from __future__ import annotations
from enum import Enum


class RoutingType(Enum):
	forwarded = "forwarded"
	lookup = "lookup"
	selfFork = "selfFork"
	unknownFutureValue = "unknownFutureValue"

