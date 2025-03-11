from __future__ import annotations
from enum import StrEnum


class RiskState(StrEnum):
	none = "none"
	confirmedSafe = "confirmedSafe"
	remediated = "remediated"
	dismissed = "dismissed"
	atRisk = "atRisk"
	confirmedCompromised = "confirmedCompromised"
	unknownFutureValue = "unknownFutureValue"

