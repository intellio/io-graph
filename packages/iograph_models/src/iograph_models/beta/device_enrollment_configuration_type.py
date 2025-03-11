from __future__ import annotations
from enum import StrEnum


class DeviceEnrollmentConfigurationType(StrEnum):
	unknown = "unknown"
	limit = "limit"
	platformRestrictions = "platformRestrictions"
	windowsHelloForBusiness = "windowsHelloForBusiness"
	defaultLimit = "defaultLimit"
	defaultPlatformRestrictions = "defaultPlatformRestrictions"
	defaultWindowsHelloForBusiness = "defaultWindowsHelloForBusiness"
	defaultWindows10EnrollmentCompletionPageConfiguration = "defaultWindows10EnrollmentCompletionPageConfiguration"
	windows10EnrollmentCompletionPageConfiguration = "windows10EnrollmentCompletionPageConfiguration"
	deviceComanagementAuthorityConfiguration = "deviceComanagementAuthorityConfiguration"
	singlePlatformRestriction = "singlePlatformRestriction"
	unknownFutureValue = "unknownFutureValue"
	enrollmentNotificationsConfiguration = "enrollmentNotificationsConfiguration"

