from __future__ import annotations
from enum import StrEnum


class OperationApprovalPolicyPlatform(StrEnum):
	notApplicable = "notApplicable"
	androidDeviceAdministrator = "androidDeviceAdministrator"
	androidEnterprise = "androidEnterprise"
	iOSiPadOS = "iOSiPadOS"
	macOS = "macOS"
	windows10AndLater = "windows10AndLater"
	windows81AndLater = "windows81AndLater"
	windows10X = "windows10X"
	unknownFutureValue = "unknownFutureValue"

