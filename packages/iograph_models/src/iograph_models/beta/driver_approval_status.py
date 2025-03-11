from __future__ import annotations
from enum import StrEnum


class DriverApprovalStatus(StrEnum):
	needsReview = "needsReview"
	declined = "declined"
	approved = "approved"
	suspended = "suspended"

