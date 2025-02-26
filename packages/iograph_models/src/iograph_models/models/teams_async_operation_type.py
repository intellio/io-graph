from __future__ import annotations
from enum import Enum


class TeamsAsyncOperationType(Enum):
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

