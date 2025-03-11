from __future__ import annotations
from enum import StrEnum


class TeamsAppInstallationScopes(StrEnum):
	team = "team"
	groupChat = "groupChat"
	personal = "personal"
	unknownFutureValue = "unknownFutureValue"

