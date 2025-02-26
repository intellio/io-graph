from __future__ import annotations
from enum import Enum


class VppTokenState(Enum):
	unknown = "unknown"
	valid = "valid"
	expired = "expired"
	invalid = "invalid"
	assignedToExternalMDM = "assignedToExternalMDM"

