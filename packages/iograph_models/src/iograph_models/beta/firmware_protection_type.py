from __future__ import annotations
from enum import StrEnum


class FirmwareProtectionType(StrEnum):
	notApplicable = "notApplicable"
	systemGuardSecureLaunch = "systemGuardSecureLaunch"
	firmwareAttackSurfaceReduction = "firmwareAttackSurfaceReduction"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

