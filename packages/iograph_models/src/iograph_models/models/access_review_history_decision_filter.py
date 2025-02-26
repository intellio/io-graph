from __future__ import annotations
from enum import Enum


class AccessReviewHistoryDecisionFilter(Enum):
	approve = "approve"
	deny = "deny"
	notReviewed = "notReviewed"
	dontKnow = "dontKnow"
	notNotified = "notNotified"
	unknownFutureValue = "unknownFutureValue"

