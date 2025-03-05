from __future__ import annotations
from enum import StrEnum


class ManagedAppDataTransferLevel(StrEnum):
	allApps = "allApps"
	managedApps = "managedApps"
	none = "none"

