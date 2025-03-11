from __future__ import annotations
from enum import StrEnum


class IosKioskModeAppType(StrEnum):
	notConfigured = "notConfigured"
	appStoreApp = "appStoreApp"
	managedApp = "managedApp"
	builtInApp = "builtInApp"

