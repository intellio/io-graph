from __future__ import annotations
from enum import StrEnum


class RegistrationAuthMethod(StrEnum):
	email = "email"
	mobilePhone = "mobilePhone"
	officePhone = "officePhone"
	securityQuestion = "securityQuestion"
	appNotification = "appNotification"
	appCode = "appCode"
	alternateMobilePhone = "alternateMobilePhone"
	fido = "fido"
	appPassword = "appPassword"
	unknownFutureValue = "unknownFutureValue"

