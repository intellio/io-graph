from __future__ import annotations
from enum import StrEnum


class TeamsAsyncOperationType(StrEnum):
	invalid = "invalid"
	cloneTeam = "cloneTeam"
	archiveTeam = "archiveTeam"
	unarchiveTeam = "unarchiveTeam"
	createTeam = "createTeam"
	unknownFutureValue = "unknownFutureValue"
	teamifyGroup = "teamifyGroup"
	createChannel = "createChannel"
	archiveChannel = "archiveChannel"
	unarchiveChannel = "unarchiveChannel"

