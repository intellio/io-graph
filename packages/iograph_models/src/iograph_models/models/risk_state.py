from __future__ import annotations
from enum import Enum


class RiskState(Enum):
	none = "none"
	confirmedSafe = "confirmedSafe"
	remediated = "remediated"
	dismissed = "dismissed"
	atRisk = "atRisk"
	confirmedCompromised = "confirmedCompromised"
	unknownFutureValue = "unknownFutureValue"

