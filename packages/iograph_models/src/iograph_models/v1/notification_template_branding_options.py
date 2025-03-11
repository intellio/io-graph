from __future__ import annotations
from enum import StrEnum


class NotificationTemplateBrandingOptions(StrEnum):
	none = "none"
	includeCompanyLogo = "includeCompanyLogo"
	includeCompanyName = "includeCompanyName"
	includeContactInformation = "includeContactInformation"
	includeCompanyPortalLink = "includeCompanyPortalLink"
	includeDeviceDetails = "includeDeviceDetails"
	unknownFutureValue = "unknownFutureValue"

