from __future__ import annotations
from enum import StrEnum


class MatchOn(StrEnum):
	displayName = "displayName"
	samAccountName = "samAccountName"
	unknownFutureValue = "unknownFutureValue"

