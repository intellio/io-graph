from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotEnrollmentType(StrEnum):
	unknown = "unknown"
	azureADJoinedWithAutopilotProfile = "azureADJoinedWithAutopilotProfile"
	offlineDomainJoined = "offlineDomainJoined"
	azureADJoinedUsingDeviceAuthWithAutopilotProfile = "azureADJoinedUsingDeviceAuthWithAutopilotProfile"
	azureADJoinedUsingDeviceAuthWithoutAutopilotProfile = "azureADJoinedUsingDeviceAuthWithoutAutopilotProfile"
	azureADJoinedWithOfflineAutopilotProfile = "azureADJoinedWithOfflineAutopilotProfile"
	azureADJoinedWithWhiteGlove = "azureADJoinedWithWhiteGlove"
	offlineDomainJoinedWithWhiteGlove = "offlineDomainJoinedWithWhiteGlove"
	offlineDomainJoinedWithOfflineAutopilotProfile = "offlineDomainJoinedWithOfflineAutopilotProfile"

