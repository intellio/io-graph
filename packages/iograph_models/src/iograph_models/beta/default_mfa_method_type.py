from __future__ import annotations
from enum import StrEnum


class DefaultMfaMethodType(StrEnum):
	none = "none"
	mobilePhone = "mobilePhone"
	alternateMobilePhone = "alternateMobilePhone"
	officePhone = "officePhone"
	microsoftAuthenticatorPush = "microsoftAuthenticatorPush"
	softwareOneTimePasscode = "softwareOneTimePasscode"
	unknownFutureValue = "unknownFutureValue"

