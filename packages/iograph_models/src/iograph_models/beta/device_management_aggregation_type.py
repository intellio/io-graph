from __future__ import annotations
from enum import StrEnum


class DeviceManagementAggregationType(StrEnum):
	count = "count"
	percentage = "percentage"
	affectedCloudPcCount = "affectedCloudPcCount"
	affectedCloudPcPercentage = "affectedCloudPcPercentage"
	unknownFutureValue = "unknownFutureValue"
	durationInMinutes = "durationInMinutes"

