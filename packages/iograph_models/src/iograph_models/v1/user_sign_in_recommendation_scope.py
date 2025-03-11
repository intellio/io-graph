from __future__ import annotations
from enum import StrEnum


class UserSignInRecommendationScope(StrEnum):
	tenant = "tenant"
	application = "application"
	unknownFutureValue = "unknownFutureValue"

