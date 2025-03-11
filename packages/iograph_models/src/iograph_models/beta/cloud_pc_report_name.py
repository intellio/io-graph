from __future__ import annotations
from enum import StrEnum


class CloudPcReportName(StrEnum):
	remoteConnectionHistoricalReports = "remoteConnectionHistoricalReports"
	dailyAggregatedRemoteConnectionReports = "dailyAggregatedRemoteConnectionReports"
	totalAggregatedRemoteConnectionReports = "totalAggregatedRemoteConnectionReports"
	unknownFutureValue = "unknownFutureValue"
	noLicenseAvailableConnectivityFailureReport = "noLicenseAvailableConnectivityFailureReport"
	frontlineLicenseUsageReport = "frontlineLicenseUsageReport"
	frontlineLicenseUsageRealTimeReport = "frontlineLicenseUsageRealTimeReport"
	remoteConnectionQualityReports = "remoteConnectionQualityReports"
	inaccessibleCloudPcReports = "inaccessibleCloudPcReports"
	actionStatusReport = "actionStatusReport"
	rawRemoteConnectionReports = "rawRemoteConnectionReports"
	cloudPcUsageCategoryReports = "cloudPcUsageCategoryReports"
	crossRegionDisasterRecoveryReport = "crossRegionDisasterRecoveryReport"
	performanceTrendReport = "performanceTrendReport"
	inaccessibleCloudPcTrendReport = "inaccessibleCloudPcTrendReport"
	regionalConnectionQualityTrendReport = "regionalConnectionQualityTrendReport"
	regionalConnectionQualityInsightsReport = "regionalConnectionQualityInsightsReport"
	remoteConnectionQualityReport = "remoteConnectionQualityReport"
	frontlineLicenseHourlyUsageReport = "frontlineLicenseHourlyUsageReport"
	frontlineRealtimeUserConnectionsReport = "frontlineRealtimeUserConnectionsReport"
	bulkActionStatusReport = "bulkActionStatusReport"
	troubleshootDetailsReport = "troubleshootDetailsReport"
	troubleshootTrendCountReport = "troubleshootTrendCountReport"
	troubleshootRegionalReport = "troubleshootRegionalReport"
	troubleshootIssueCountReport = "troubleshootIssueCountReport"
	cloudPcInsightReport = "cloudPcInsightReport"
	regionalInaccessibleCloudPcTrendReport = "regionalInaccessibleCloudPcTrendReport"

