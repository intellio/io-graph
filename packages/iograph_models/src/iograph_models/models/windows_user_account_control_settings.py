from __future__ import annotations
from enum import Enum


class WindowsUserAccountControlSettings(Enum):
	userDefined = "userDefined"
	alwaysNotify = "alwaysNotify"
	notifyOnAppChanges = "notifyOnAppChanges"
	notifyOnAppChangesWithoutDimming = "notifyOnAppChangesWithoutDimming"
	neverNotify = "neverNotify"

