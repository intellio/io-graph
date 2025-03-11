from __future__ import annotations
from enum import StrEnum


class ManagedAppPhoneNumberRedirectLevel(StrEnum):
	allApps = "allApps"
	managedApps = "managedApps"
	customApp = "customApp"
	blocked = "blocked"

