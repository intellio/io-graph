from __future__ import annotations
from enum import StrEnum


class SecurityAntispamDirectionality(StrEnum):
	unknown = "unknown"
	inbound = "inbound"
	outbound = "outbound"
	intraOrg = "intraOrg"
	unknownFutureValue = "unknownFutureValue"

