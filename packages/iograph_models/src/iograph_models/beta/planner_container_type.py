from __future__ import annotations
from enum import StrEnum


class PlannerContainerType(StrEnum):
	group = "group"
	unknownFutureValue = "unknownFutureValue"
	roster = "roster"
	project = "project"
	driveItem = "driveItem"
	user = "user"
	teamsChannel = "teamsChannel"

