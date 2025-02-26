from __future__ import annotations
from enum import Enum


class CallRecordsClientPlatform(Enum):
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

