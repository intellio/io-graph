from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsSummarizedBy(StrEnum):
	none = "none"
	model = "model"
	allRegressions = "allRegressions"
	modelRegression = "modelRegression"
	manufacturerRegression = "manufacturerRegression"
	operatingSystemVersionRegression = "operatingSystemVersionRegression"
	unknownFutureValue = "unknownFutureValue"

