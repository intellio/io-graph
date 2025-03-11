from __future__ import annotations
from enum import StrEnum


class TeamworkSupportedClient(StrEnum):
	unknown = "unknown"
	skypeDefaultAndTeams = "skypeDefaultAndTeams"
	teamsDefaultAndSkype = "teamsDefaultAndSkype"
	skypeOnly = "skypeOnly"
	teamsOnly = "teamsOnly"
	unknownFutureValue = "unknownFutureValue"

