from __future__ import annotations
from enum import StrEnum


class IosWallpaperDisplayLocation(StrEnum):
	notConfigured = "notConfigured"
	lockScreen = "lockScreen"
	homeScreen = "homeScreen"
	lockAndHomeScreens = "lockAndHomeScreens"

