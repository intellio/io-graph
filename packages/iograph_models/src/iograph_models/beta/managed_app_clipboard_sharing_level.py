from __future__ import annotations
from enum import StrEnum


class ManagedAppClipboardSharingLevel(StrEnum):
	allApps = "allApps"
	managedAppsWithPasteIn = "managedAppsWithPasteIn"
	managedApps = "managedApps"
	blocked = "blocked"

