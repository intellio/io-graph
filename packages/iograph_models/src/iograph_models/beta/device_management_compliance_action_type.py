from __future__ import annotations
from enum import StrEnum


class DeviceManagementComplianceActionType(StrEnum):
	noAction = "noAction"
	notification = "notification"
	block = "block"
	retire = "retire"
	wipe = "wipe"
	removeResourceAccessProfiles = "removeResourceAccessProfiles"
	pushNotification = "pushNotification"
	remoteLock = "remoteLock"

