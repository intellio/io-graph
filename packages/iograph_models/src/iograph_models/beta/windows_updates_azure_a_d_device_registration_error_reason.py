from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesAzureADDeviceRegistrationErrorReason(StrEnum):
	invalidGlobalDeviceId = "invalidGlobalDeviceId"
	invalidAzureADDeviceId = "invalidAzureADDeviceId"
	missingTrustType = "missingTrustType"
	invalidAzureADJoin = "invalidAzureADJoin"
	unknownFutureValue = "unknownFutureValue"

