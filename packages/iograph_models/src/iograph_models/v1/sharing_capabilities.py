from __future__ import annotations
from enum import StrEnum


class SharingCapabilities(StrEnum):
	disabled = "disabled"
	externalUserSharingOnly = "externalUserSharingOnly"
	externalUserAndGuestSharing = "externalUserAndGuestSharing"
	existingExternalUserSharingOnly = "existingExternalUserSharingOnly"
	unknownFutureValue = "unknownFutureValue"

