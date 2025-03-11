from __future__ import annotations
from enum import StrEnum


class AndroidManagedStoreAccountEnrollmentTarget(StrEnum):
	none = "none"
	all = "all"
	targeted = "targeted"
	targetedAsEnrollmentRestrictions = "targetedAsEnrollmentRestrictions"

