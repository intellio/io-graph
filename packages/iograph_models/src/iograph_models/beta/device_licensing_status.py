from __future__ import annotations
from enum import StrEnum


class DeviceLicensingStatus(StrEnum):
	unknown = "unknown"
	licenseRefreshStarted = "licenseRefreshStarted"
	licenseRefreshPending = "licenseRefreshPending"
	deviceIsNotAzureActiveDirectoryJoined = "deviceIsNotAzureActiveDirectoryJoined"
	verifyingMicrosoftDeviceIdentity = "verifyingMicrosoftDeviceIdentity"
	deviceIdentityVerificationFailed = "deviceIdentityVerificationFailed"
	verifyingMicrosoftAccountIdentity = "verifyingMicrosoftAccountIdentity"
	microsoftAccountVerificationFailed = "microsoftAccountVerificationFailed"
	acquiringDeviceLicense = "acquiringDeviceLicense"
	refreshingDeviceLicense = "refreshingDeviceLicense"
	deviceLicenseRefreshSucceed = "deviceLicenseRefreshSucceed"
	deviceLicenseRefreshFailed = "deviceLicenseRefreshFailed"
	removingDeviceLicense = "removingDeviceLicense"
	deviceLicenseRemoveSucceed = "deviceLicenseRemoveSucceed"
	deviceLicenseRemoveFailed = "deviceLicenseRemoveFailed"
	unknownFutureValue = "unknownFutureValue"

