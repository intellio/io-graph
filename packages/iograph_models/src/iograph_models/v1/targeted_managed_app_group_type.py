from __future__ import annotations
from enum import StrEnum


class TargetedManagedAppGroupType(StrEnum):
	selectedPublicApps = "selectedPublicApps"
	allCoreMicrosoftApps = "allCoreMicrosoftApps"
	allMicrosoftApps = "allMicrosoftApps"
	allApps = "allApps"

