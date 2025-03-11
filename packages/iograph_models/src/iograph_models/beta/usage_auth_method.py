from __future__ import annotations
from enum import StrEnum


class UsageAuthMethod(StrEnum):
	email = "email"
	mobileSMS = "mobileSMS"
	mobileCall = "mobileCall"
	officePhone = "officePhone"
	securityQuestion = "securityQuestion"
	appNotification = "appNotification"
	appCode = "appCode"
	alternateMobileCall = "alternateMobileCall"
	fido = "fido"
	appPassword = "appPassword"
	unknownFutureValue = "unknownFutureValue"

