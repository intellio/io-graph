from __future__ import annotations
from enum import StrEnum


class EducationSubmissionStatus(StrEnum):
	working = "working"
	submitted = "submitted"
	released = "released"
	returned = "returned"
	unknownFutureValue = "unknownFutureValue"
	reassigned = "reassigned"
	excused = "excused"

