from __future__ import annotations
from enum import StrEnum


class EducationAddToCalendarOptions(StrEnum):
	none = "none"
	studentsAndPublisher = "studentsAndPublisher"
	studentsAndTeamOwners = "studentsAndTeamOwners"
	unknownFutureValue = "unknownFutureValue"
	studentsOnly = "studentsOnly"

