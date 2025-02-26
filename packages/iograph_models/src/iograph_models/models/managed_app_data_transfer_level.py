from __future__ import annotations
from enum import Enum


class ManagedAppDataTransferLevel(Enum):
	allApps = "allApps"
	managedApps = "managedApps"
	none = "none"

