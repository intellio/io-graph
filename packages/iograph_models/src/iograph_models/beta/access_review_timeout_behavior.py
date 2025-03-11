from __future__ import annotations
from enum import StrEnum


class AccessReviewTimeoutBehavior(StrEnum):
	keepAccess = "keepAccess"
	removeAccess = "removeAccess"
	acceptAccessRecommendation = "acceptAccessRecommendation"
	unknownFutureValue = "unknownFutureValue"

