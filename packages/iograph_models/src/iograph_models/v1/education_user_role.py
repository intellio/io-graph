from __future__ import annotations
from enum import StrEnum


class EducationUserRole(StrEnum):
	student = "student"
	teacher = "teacher"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

