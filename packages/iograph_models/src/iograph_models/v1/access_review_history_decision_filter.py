from __future__ import annotations
from enum import StrEnum


class AccessReviewHistoryDecisionFilter(StrEnum):
	approve = "approve"
	deny = "deny"
	notReviewed = "notReviewed"
	dontKnow = "dontKnow"
	notNotified = "notNotified"
	unknownFutureValue = "unknownFutureValue"

