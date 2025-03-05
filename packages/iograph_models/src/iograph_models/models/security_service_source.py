from __future__ import annotations
from enum import StrEnum


class SecurityServiceSource(StrEnum):
	unknown = "unknown"
	microsoftDefenderForEndpoint = "microsoftDefenderForEndpoint"
	microsoftDefenderForIdentity = "microsoftDefenderForIdentity"
	microsoftDefenderForCloudApps = "microsoftDefenderForCloudApps"
	microsoftDefenderForOffice365 = "microsoftDefenderForOffice365"
	microsoft365Defender = "microsoft365Defender"
	azureAdIdentityProtection = "azureAdIdentityProtection"
	microsoftAppGovernance = "microsoftAppGovernance"
	dataLossPrevention = "dataLossPrevention"
	unknownFutureValue = "unknownFutureValue"
	microsoftDefenderForCloud = "microsoftDefenderForCloud"
	microsoftSentinel = "microsoftSentinel"
	microsoftInsiderRiskManagement = "microsoftInsiderRiskManagement"

