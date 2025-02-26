from __future__ import annotations
from enum import Enum


class DataSubjectType(Enum):
	customer = "customer"
	currentEmployee = "currentEmployee"
	formerEmployee = "formerEmployee"
	prospectiveEmployee = "prospectiveEmployee"
	student = "student"
	teacher = "teacher"
	faculty = "faculty"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

