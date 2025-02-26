from __future__ import annotations
from enum import Enum


class NotificationTemplateBrandingOptions(Enum):
	none = "none"
	includeCompanyLogo = "includeCompanyLogo"
	includeCompanyName = "includeCompanyName"
	includeContactInformation = "includeContactInformation"
	includeCompanyPortalLink = "includeCompanyPortalLink"
	includeDeviceDetails = "includeDeviceDetails"
	unknownFutureValue = "unknownFutureValue"

