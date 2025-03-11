from __future__ import annotations
from enum import StrEnum


class SharedPCAccountDeletionPolicyType(StrEnum):
	immediate = "immediate"
	diskSpaceThreshold = "diskSpaceThreshold"
	diskSpaceThresholdOrInactiveThreshold = "diskSpaceThresholdOrInactiveThreshold"

