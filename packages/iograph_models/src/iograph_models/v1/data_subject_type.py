from __future__ import annotations
from enum import StrEnum


class DataSubjectType(StrEnum):
	customer = "customer"
	currentEmployee = "currentEmployee"
	formerEmployee = "formerEmployee"
	prospectiveEmployee = "prospectiveEmployee"
	student = "student"
	teacher = "teacher"
	faculty = "faculty"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

