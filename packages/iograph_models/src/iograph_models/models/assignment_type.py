from __future__ import annotations
from enum import Enum


class AssignmentType(Enum):
	required = "required"
	recommended = "recommended"
	unknownFutureValue = "unknownFutureValue"
	peerRecommended = "peerRecommended"

