from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerCrossProfileDataSharing(StrEnum):
	notConfigured = "notConfigured"
	crossProfileDataSharingBlocked = "crossProfileDataSharingBlocked"
	dataSharingFromWorkToPersonalBlocked = "dataSharingFromWorkToPersonalBlocked"
	crossProfileDataSharingAllowed = "crossProfileDataSharingAllowed"
	unkownFutureValue = "unkownFutureValue"

