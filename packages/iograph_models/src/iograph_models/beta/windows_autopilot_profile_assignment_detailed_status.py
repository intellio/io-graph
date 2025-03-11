from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotProfileAssignmentDetailedStatus(StrEnum):
	none = "none"
	hardwareRequirementsNotMet = "hardwareRequirementsNotMet"
	surfaceHubProfileNotSupported = "surfaceHubProfileNotSupported"
	holoLensProfileNotSupported = "holoLensProfileNotSupported"
	windowsPcProfileNotSupported = "windowsPcProfileNotSupported"
	surfaceHub2SProfileNotSupported = "surfaceHub2SProfileNotSupported"
	unknownFutureValue = "unknownFutureValue"

