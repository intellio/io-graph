from __future__ import annotations
from enum import Enum


class SharedPCAccountDeletionPolicyType(Enum):
	immediate = "immediate"
	diskSpaceThreshold = "diskSpaceThreshold"
	diskSpaceThresholdOrInactiveThreshold = "diskSpaceThresholdOrInactiveThreshold"

