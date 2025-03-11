from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoDataRetentionPolicy(StrEnum):
	dataRetained = "dataRetained"
	deletedImmediately = "deletedImmediately"
	deletedWithinTwoWeeks = "deletedWithinTwoWeeks"
	deletedWithinOneMonth = "deletedWithinOneMonth"
	deletedWithinThreeMonths = "deletedWithinThreeMonths"
	deletedWithinMoreThanThreeMonths = "deletedWithinMoreThanThreeMonths"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

