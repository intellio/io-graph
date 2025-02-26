from __future__ import annotations
from enum import Enum


class UserExperienceAnalyticsSummarizedBy(Enum):
	none = "none"
	model = "model"
	allRegressions = "allRegressions"
	modelRegression = "modelRegression"
	manufacturerRegression = "manufacturerRegression"
	operatingSystemVersionRegression = "operatingSystemVersionRegression"
	unknownFutureValue = "unknownFutureValue"

