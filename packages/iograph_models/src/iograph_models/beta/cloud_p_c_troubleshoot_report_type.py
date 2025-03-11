from __future__ import annotations
from enum import StrEnum


class CloudPCTroubleshootReportType(StrEnum):
	troubleshootDetailsReport = "troubleshootDetailsReport"
	troubleshootTrendCountReport = "troubleshootTrendCountReport"
	troubleshootRegionalReport = "troubleshootRegionalReport"
	unknownFutureValue = "unknownFutureValue"
	troubleshootIssueCountReport = "troubleshootIssueCountReport"

