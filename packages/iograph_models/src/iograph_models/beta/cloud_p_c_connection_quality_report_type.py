from __future__ import annotations
from enum import StrEnum


class CloudPCConnectionQualityReportType(StrEnum):
	remoteConnectionQualityReport = "remoteConnectionQualityReport"
	regionalConnectionQualityTrendReport = "regionalConnectionQualityTrendReport"
	regionalConnectionQualityInsightsReport = "regionalConnectionQualityInsightsReport"
	unknownFutureValue = "unknownFutureValue"

