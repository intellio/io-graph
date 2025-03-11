from __future__ import annotations
from enum import StrEnum


class CloudPcDisasterRecoveryType(StrEnum):
	notConfigured = "notConfigured"
	crossRegion = "crossRegion"
	premium = "premium"
	unknownFutureValue = "unknownFutureValue"

