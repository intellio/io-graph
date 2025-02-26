from __future__ import annotations
from enum import Enum


class TermStoreRelationType(Enum):
	pin = "pin"
	reuse = "reuse"
	unknownFutureValue = "unknownFutureValue"

