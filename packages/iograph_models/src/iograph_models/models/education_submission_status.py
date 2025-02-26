from __future__ import annotations
from enum import Enum


class EducationSubmissionStatus(Enum):
	working = "working"
	submitted = "submitted"
	released = "released"
	returned = "returned"
	unknownFutureValue = "unknownFutureValue"
	reassigned = "reassigned"
	excused = "excused"

