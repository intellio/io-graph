from __future__ import annotations
from enum import StrEnum


class AssignmentFilterEvaluationResult(StrEnum):
	unknown = "unknown"
	match = "match"
	notMatch = "notMatch"
	inconclusive = "inconclusive"
	failure = "failure"
	notEvaluated = "notEvaluated"

