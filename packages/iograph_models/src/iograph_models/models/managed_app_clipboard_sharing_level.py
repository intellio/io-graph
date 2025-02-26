from __future__ import annotations
from enum import Enum


class ManagedAppClipboardSharingLevel(Enum):
	allApps = "allApps"
	managedAppsWithPasteIn = "managedAppsWithPasteIn"
	managedApps = "managedApps"
	blocked = "blocked"

