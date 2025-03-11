from __future__ import annotations
from enum import StrEnum


class DeviceManagementAutopilotPolicyComplianceStatus(StrEnum):
	unknown = "unknown"
	compliant = "compliant"
	installed = "installed"
	notCompliant = "notCompliant"
	notInstalled = "notInstalled"
	error = "error"

