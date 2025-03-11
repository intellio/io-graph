from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsAnomalyDeviceFeatureType(StrEnum):
	manufacturer = "manufacturer"
	model = "model"
	osVersion = "osVersion"
	application = "application"
	driver = "driver"
	unknownFutureValue = "unknownFutureValue"

