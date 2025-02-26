from __future__ import annotations
from enum import Enum


class SharingCapabilities(Enum):
	disabled = "disabled"
	externalUserSharingOnly = "externalUserSharingOnly"
	externalUserAndGuestSharing = "externalUserAndGuestSharing"
	existingExternalUserSharingOnly = "existingExternalUserSharingOnly"
	unknownFutureValue = "unknownFutureValue"

