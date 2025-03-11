from __future__ import annotations
from enum import StrEnum


class AssignmentType(StrEnum):
	required = "required"
	recommended = "recommended"
	unknownFutureValue = "unknownFutureValue"
	peerRecommended = "peerRecommended"

