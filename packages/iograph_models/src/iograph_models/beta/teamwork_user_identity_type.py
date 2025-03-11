from __future__ import annotations
from enum import StrEnum


class TeamworkUserIdentityType(StrEnum):
	aadUser = "aadUser"
	onPremiseAadUser = "onPremiseAadUser"
	anonymousGuest = "anonymousGuest"
	federatedUser = "federatedUser"
	personalMicrosoftAccountUser = "personalMicrosoftAccountUser"
	skypeUser = "skypeUser"
	phoneUser = "phoneUser"
	unknownFutureValue = "unknownFutureValue"
	emailUser = "emailUser"
	azureCommunicationServicesUser = "azureCommunicationServicesUser"

