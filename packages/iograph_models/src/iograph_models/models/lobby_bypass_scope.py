from __future__ import annotations
from enum import Enum


class LobbyBypassScope(Enum):
	organizer = "organizer"
	organization = "organization"
	organizationAndFederated = "organizationAndFederated"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"
	invited = "invited"
	organizationExcludingGuests = "organizationExcludingGuests"

