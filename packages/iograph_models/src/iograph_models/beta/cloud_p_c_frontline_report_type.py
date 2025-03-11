from __future__ import annotations
from enum import StrEnum


class CloudPCFrontlineReportType(StrEnum):
	noLicenseAvailableConnectivityFailureReport = "noLicenseAvailableConnectivityFailureReport"
	licenseUsageReport = "licenseUsageReport"
	licenseUsageRealTimeReport = "licenseUsageRealTimeReport"
	licenseHourlyUsageReport = "licenseHourlyUsageReport"
	connectedUserRealtimeReport = "connectedUserRealtimeReport"
	unknownFutureValue = "unknownFutureValue"

