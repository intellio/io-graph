from __future__ import annotations
from enum import StrEnum


class CallRecordsClientPlatform(StrEnum):
	unknown = "unknown"
	windows = "windows"
	macOS = "macOS"
	iOS = "iOS"
	android = "android"
	web = "web"
	ipPhone = "ipPhone"
	roomSystem = "roomSystem"
	surfaceHub = "surfaceHub"
	holoLens = "holoLens"
	unknownFutureValue = "unknownFutureValue"

