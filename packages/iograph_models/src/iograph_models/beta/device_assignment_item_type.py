from __future__ import annotations
from enum import StrEnum


class DeviceAssignmentItemType(StrEnum):
	application = "application"
	deviceConfiguration = "deviceConfiguration"
	deviceManagementConfigurationPolicy = "deviceManagementConfigurationPolicy"
	mobileAppConfiguration = "mobileAppConfiguration"
	unknownFutureValue = "unknownFutureValue"

