from __future__ import annotations
from enum import StrEnum


class WindowsUserAccountControlSettings(StrEnum):
	userDefined = "userDefined"
	alwaysNotify = "alwaysNotify"
	notifyOnAppChanges = "notifyOnAppChanges"
	notifyOnAppChangesWithoutDimming = "notifyOnAppChangesWithoutDimming"
	neverNotify = "neverNotify"

