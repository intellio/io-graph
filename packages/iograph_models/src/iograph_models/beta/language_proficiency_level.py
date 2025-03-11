from __future__ import annotations
from enum import StrEnum


class LanguageProficiencyLevel(StrEnum):
	elementary = "elementary"
	conversational = "conversational"
	limitedWorking = "limitedWorking"
	professionalWorking = "professionalWorking"
	fullProfessional = "fullProfessional"
	nativeOrBilingual = "nativeOrBilingual"
	unknownFutureValue = "unknownFutureValue"

