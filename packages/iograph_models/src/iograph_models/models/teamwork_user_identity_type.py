from __future__ import annotations
from enum import Enum


class TeamworkUserIdentityType(Enum):
	aadUser = "aadUser"
	onPremiseAadUser = "onPremiseAadUser"
	anonymousGuest = "anonymousGuest"
	federatedUser = "federatedUser"
	personalMicrosoftAccountUser = "personalMicrosoftAccountUser"
	skypeUser = "skypeUser"
	phoneUser = "phoneUser"
	unknownFutureValue = "unknownFutureValue"
	emailUser = "emailUser"

