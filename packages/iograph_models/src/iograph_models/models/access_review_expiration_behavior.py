from __future__ import annotations
from enum import Enum


class AccessReviewExpirationBehavior(Enum):
	keepAccess = "keepAccess"
	removeAccess = "removeAccess"
	acceptAccessRecommendation = "acceptAccessRecommendation"
	unknownFutureValue = "unknownFutureValue"

