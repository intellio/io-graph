from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesEnrollmentState(StrEnum):
	notEnrolled = "notEnrolled"
	enrolled = "enrolled"
	enrolledWithPolicy = "enrolledWithPolicy"
	enrolling = "enrolling"
	unenrolling = "unenrolling"
	unknownFutureValue = "unknownFutureValue"

