from __future__ import annotations
from enum import StrEnum


class RoutingType(StrEnum):
	forwarded = "forwarded"
	lookup = "lookup"
	selfFork = "selfFork"
	unknownFutureValue = "unknownFutureValue"

