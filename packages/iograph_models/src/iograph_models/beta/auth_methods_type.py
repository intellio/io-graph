from __future__ import annotations
from enum import StrEnum


class AuthMethodsType(StrEnum):
	email = "email"
	mobileSMS = "mobileSMS"
	mobilePhone = "mobilePhone"
	officePhone = "officePhone"
	securityQuestion = "securityQuestion"
	appNotification = "appNotification"
	appNotificationCode = "appNotificationCode"
	appNotificationAndCode = "appNotificationAndCode"
	appPassword = "appPassword"
	fido = "fido"
	alternateMobilePhone = "alternateMobilePhone"
	mobilePhoneAndSMS = "mobilePhoneAndSMS"
	unknownFutureValue = "unknownFutureValue"

