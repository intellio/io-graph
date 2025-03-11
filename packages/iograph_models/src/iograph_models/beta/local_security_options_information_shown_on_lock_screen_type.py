from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsInformationShownOnLockScreenType(StrEnum):
	notConfigured = "notConfigured"
	userDisplayNameDomainUser = "userDisplayNameDomainUser"
	userDisplayNameOnly = "userDisplayNameOnly"
	doNotDisplayUser = "doNotDisplayUser"

