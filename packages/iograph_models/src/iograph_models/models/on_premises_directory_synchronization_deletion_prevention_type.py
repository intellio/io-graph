from __future__ import annotations
from enum import Enum


class OnPremisesDirectorySynchronizationDeletionPreventionType(Enum):
	disabled = "disabled"
	enabledForCount = "enabledForCount"
	enabledForPercentage = "enabledForPercentage"
	unknownFutureValue = "unknownFutureValue"

