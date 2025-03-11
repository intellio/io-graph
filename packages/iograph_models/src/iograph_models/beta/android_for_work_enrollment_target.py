from __future__ import annotations
from enum import StrEnum


class AndroidForWorkEnrollmentTarget(StrEnum):
	none = "none"
	all = "all"
	targeted = "targeted"
	targetedAsEnrollmentRestrictions = "targetedAsEnrollmentRestrictions"

