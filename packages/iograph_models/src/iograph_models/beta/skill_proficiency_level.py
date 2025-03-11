from __future__ import annotations
from enum import StrEnum


class SkillProficiencyLevel(StrEnum):
	elementary = "elementary"
	limitedWorking = "limitedWorking"
	generalProfessional = "generalProfessional"
	advancedProfessional = "advancedProfessional"
	expert = "expert"
	unknownFutureValue = "unknownFutureValue"

