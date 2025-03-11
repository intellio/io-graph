from __future__ import annotations
from enum import StrEnum


class VppTokenState(StrEnum):
	unknown = "unknown"
	valid = "valid"
	expired = "expired"
	invalid = "invalid"
	assignedToExternalMDM = "assignedToExternalMDM"

