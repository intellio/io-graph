from __future__ import annotations
from enum import StrEnum


class LobbyBypassScope(StrEnum):
	organizer = "organizer"
	organization = "organization"
	organizationAndFederated = "organizationAndFederated"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"
	invited = "invited"
	organizationExcludingGuests = "organizationExcludingGuests"

