from __future__ import annotations
from enum import Enum


class TargetedManagedAppGroupType(Enum):
	selectedPublicApps = "selectedPublicApps"
	allCoreMicrosoftApps = "allCoreMicrosoftApps"
	allMicrosoftApps = "allMicrosoftApps"
	allApps = "allApps"

