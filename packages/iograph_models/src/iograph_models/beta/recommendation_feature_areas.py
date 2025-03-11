from __future__ import annotations
from enum import StrEnum


class RecommendationFeatureAreas(StrEnum):
	users = "users"
	groups = "groups"
	devices = "devices"
	applications = "applications"
	accessReviews = "accessReviews"
	conditionalAccess = "conditionalAccess"
	governance = "governance"
	unknownFutureValue = "unknownFutureValue"

