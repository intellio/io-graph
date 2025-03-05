from __future__ import annotations
from enum import StrEnum


class DeviceManagementExchangeAccessStateReason(StrEnum):
	none = "none"
	unknown = "unknown"
	exchangeGlobalRule = "exchangeGlobalRule"
	exchangeIndividualRule = "exchangeIndividualRule"
	exchangeDeviceRule = "exchangeDeviceRule"
	exchangeUpgrade = "exchangeUpgrade"
	exchangeMailboxPolicy = "exchangeMailboxPolicy"
	other = "other"
	compliant = "compliant"
	notCompliant = "notCompliant"
	notEnrolled = "notEnrolled"
	unknownLocation = "unknownLocation"
	mfaRequired = "mfaRequired"
	azureADBlockDueToAccessPolicy = "azureADBlockDueToAccessPolicy"
	compromisedPassword = "compromisedPassword"
	deviceNotKnownWithManagedApp = "deviceNotKnownWithManagedApp"

