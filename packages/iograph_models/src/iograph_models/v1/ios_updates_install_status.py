from __future__ import annotations
from enum import StrEnum


class IosUpdatesInstallStatus(StrEnum):
	deviceOsHigherThanDesiredOsVersion = "deviceOsHigherThanDesiredOsVersion"
	sharedDeviceUserLoggedInError = "sharedDeviceUserLoggedInError"
	notSupportedOperation = "notSupportedOperation"
	installFailed = "installFailed"
	installPhoneCallInProgress = "installPhoneCallInProgress"
	installInsufficientPower = "installInsufficientPower"
	installInsufficientSpace = "installInsufficientSpace"
	installing = "installing"
	downloadInsufficientNetwork = "downloadInsufficientNetwork"
	downloadInsufficientPower = "downloadInsufficientPower"
	downloadInsufficientSpace = "downloadInsufficientSpace"
	downloadRequiresComputer = "downloadRequiresComputer"
	downloadFailed = "downloadFailed"
	downloading = "downloading"
	success = "success"
	available = "available"
	idle = "idle"
	unknown = "unknown"

