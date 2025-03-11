from __future__ import annotations
from enum import StrEnum


class FrontlineCloudPcAccessState(StrEnum):
	unassigned = "unassigned"
	noLicensesAvailable = "noLicensesAvailable"
	activationFailed = "activationFailed"
	active = "active"
	activating = "activating"
	standbyMode = "standbyMode"
	unknownFutureValue = "unknownFutureValue"

