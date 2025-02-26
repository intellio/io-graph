from __future__ import annotations
from enum import Enum


class ConditionalAccessGuestOrExternalUserTypes(Enum):
	none = "none"
	internalGuest = "internalGuest"
	b2bCollaborationGuest = "b2bCollaborationGuest"
	b2bCollaborationMember = "b2bCollaborationMember"
	b2bDirectConnectUser = "b2bDirectConnectUser"
	otherExternalUser = "otherExternalUser"
	serviceProvider = "serviceProvider"
	unknownFutureValue = "unknownFutureValue"

