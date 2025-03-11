from __future__ import annotations
from enum import StrEnum


class AllowedAudiences(StrEnum):
	me = "me"
	family = "family"
	contacts = "contacts"
	groupMembers = "groupMembers"
	organization = "organization"
	federatedOrganizations = "federatedOrganizations"
	everyone = "everyone"
	unknownFutureValue = "unknownFutureValue"

