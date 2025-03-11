from __future__ import annotations
from enum import StrEnum


class EnrollmentAvailabilityOptions(StrEnum):
	availableWithPrompts = "availableWithPrompts"
	availableWithoutPrompts = "availableWithoutPrompts"
	unavailable = "unavailable"

