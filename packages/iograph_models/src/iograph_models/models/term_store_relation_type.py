from __future__ import annotations
from enum import StrEnum


class TermStoreRelationType(StrEnum):
	pin = "pin"
	reuse = "reuse"
	unknownFutureValue = "unknownFutureValue"

