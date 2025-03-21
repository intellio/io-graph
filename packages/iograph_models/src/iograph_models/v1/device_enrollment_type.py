from __future__ import annotations
from enum import StrEnum


class DeviceEnrollmentType(StrEnum):
	unknown = "unknown"
	userEnrollment = "userEnrollment"
	deviceEnrollmentManager = "deviceEnrollmentManager"
	appleBulkWithUser = "appleBulkWithUser"
	appleBulkWithoutUser = "appleBulkWithoutUser"
	windowsAzureADJoin = "windowsAzureADJoin"
	windowsBulkUserless = "windowsBulkUserless"
	windowsAutoEnrollment = "windowsAutoEnrollment"
	windowsBulkAzureDomainJoin = "windowsBulkAzureDomainJoin"
	windowsCoManagement = "windowsCoManagement"
	windowsAzureADJoinUsingDeviceAuth = "windowsAzureADJoinUsingDeviceAuth"
	appleUserEnrollment = "appleUserEnrollment"
	appleUserEnrollmentWithServiceAccount = "appleUserEnrollmentWithServiceAccount"

