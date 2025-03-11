from __future__ import annotations
from enum import StrEnum


class ThreatAssessmentRequestSource(StrEnum):
	undefined = "undefined"
	user = "user"
	administrator = "administrator"

