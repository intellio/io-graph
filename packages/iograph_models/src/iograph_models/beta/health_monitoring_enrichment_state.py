from __future__ import annotations
from enum import StrEnum


class HealthMonitoringEnrichmentState(StrEnum):
	none = "none"
	inProgress = "inProgress"
	enriched = "enriched"
	unknownFutureValue = "unknownFutureValue"

