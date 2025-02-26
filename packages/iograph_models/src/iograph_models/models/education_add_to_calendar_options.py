from __future__ import annotations
from enum import Enum


class EducationAddToCalendarOptions(Enum):
	none = "none"
	studentsAndPublisher = "studentsAndPublisher"
	studentsAndTeamOwners = "studentsAndTeamOwners"
	unknownFutureValue = "unknownFutureValue"
	studentsOnly = "studentsOnly"

