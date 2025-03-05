from __future__ import annotations
from enum import StrEnum


class AllowedLobbyAdmitterRoles(StrEnum):
	organizerAndCoOrganizersAndPresenters = "organizerAndCoOrganizersAndPresenters"
	organizerAndCoOrganizers = "organizerAndCoOrganizers"
	unknownFutureValue = "unknownFutureValue"

