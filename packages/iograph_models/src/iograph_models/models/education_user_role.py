from __future__ import annotations
from enum import Enum


class EducationUserRole(Enum):
	student = "student"
	teacher = "teacher"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

