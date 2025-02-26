from __future__ import annotations
from enum import Enum


class DeviceComplianceActionType(Enum):
	noAction = "noAction"
	notification = "notification"
	block = "block"
	retire = "retire"
	wipe = "wipe"
	removeResourceAccessProfiles = "removeResourceAccessProfiles"
	pushNotification = "pushNotification"

