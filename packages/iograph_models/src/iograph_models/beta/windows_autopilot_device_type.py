from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotDeviceType(StrEnum):
	windowsPc = "windowsPc"
	holoLens = "holoLens"
	surfaceHub2 = "surfaceHub2"
	surfaceHub2S = "surfaceHub2S"
	virtualMachine = "virtualMachine"
	unknownFutureValue = "unknownFutureValue"

