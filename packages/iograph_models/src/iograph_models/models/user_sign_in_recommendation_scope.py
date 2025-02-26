from __future__ import annotations
from enum import Enum


class UserSignInRecommendationScope(Enum):
	tenant = "tenant"
	application = "application"
	unknownFutureValue = "unknownFutureValue"

