from __future__ import annotations
from enum import StrEnum


class EnrollmentNotificationBrandingOptions(StrEnum):
	none = "none"
	includeCompanyLogo = "includeCompanyLogo"
	includeCompanyName = "includeCompanyName"
	includeContactInformation = "includeContactInformation"
	includeCompanyPortalLink = "includeCompanyPortalLink"
	includeDeviceDetails = "includeDeviceDetails"
	unknownFutureValue = "unknownFutureValue"

