from __future__ import annotations
from enum import StrEnum


class SecurityAntispamTeamsDirection(StrEnum):
	unknown = "unknown"
	inbound = "inbound"
	outbound = "outbound"
	intraorg = "intraorg"
	unknownFutureValue = "unknownFutureValue"

