from __future__ import annotations
from enum import StrEnum


class PlannerPlanContextType(StrEnum):
	teamsTab = "teamsTab"
	sharePointPage = "sharePointPage"
	meetingNotes = "meetingNotes"
	other = "other"
	unknownFutureValue = "unknownFutureValue"
	loopPage = "loopPage"
	project = "project"

