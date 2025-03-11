from __future__ import annotations
from enum import StrEnum


class OnPremisesDirectorySynchronizationDeletionPreventionType(StrEnum):
	disabled = "disabled"
	enabledForCount = "enabledForCount"
	enabledForPercentage = "enabledForPercentage"
	unknownFutureValue = "unknownFutureValue"

