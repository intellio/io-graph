from __future__ import annotations
from enum import StrEnum


class SecurityDetectionSource(StrEnum):
	unknown = "unknown"
	microsoftDefenderForEndpoint = "microsoftDefenderForEndpoint"
	antivirus = "antivirus"
	smartScreen = "smartScreen"
	customTi = "customTi"
	microsoftDefenderForOffice365 = "microsoftDefenderForOffice365"
	automatedInvestigation = "automatedInvestigation"
	microsoftThreatExperts = "microsoftThreatExperts"
	customDetection = "customDetection"
	microsoftDefenderForIdentity = "microsoftDefenderForIdentity"
	cloudAppSecurity = "cloudAppSecurity"
	microsoft365Defender = "microsoft365Defender"
	azureAdIdentityProtection = "azureAdIdentityProtection"
	manual = "manual"
	microsoftDataLossPrevention = "microsoftDataLossPrevention"
	appGovernancePolicy = "appGovernancePolicy"
	appGovernanceDetection = "appGovernanceDetection"
	unknownFutureValue = "unknownFutureValue"
	microsoftDefenderForCloud = "microsoftDefenderForCloud"
	microsoftDefenderForIoT = "microsoftDefenderForIoT"
	microsoftDefenderForServers = "microsoftDefenderForServers"
	microsoftDefenderForStorage = "microsoftDefenderForStorage"
	microsoftDefenderForDNS = "microsoftDefenderForDNS"
	microsoftDefenderForDatabases = "microsoftDefenderForDatabases"
	microsoftDefenderForContainers = "microsoftDefenderForContainers"
	microsoftDefenderForNetwork = "microsoftDefenderForNetwork"
	microsoftDefenderForAppService = "microsoftDefenderForAppService"
	microsoftDefenderForKeyVault = "microsoftDefenderForKeyVault"
	microsoftDefenderForResourceManager = "microsoftDefenderForResourceManager"
	microsoftDefenderForApiManagement = "microsoftDefenderForApiManagement"
	nrtAlerts = "nrtAlerts"
	scheduledAlerts = "scheduledAlerts"
	microsoftDefenderThreatIntelligenceAnalytics = "microsoftDefenderThreatIntelligenceAnalytics"
	builtInMl = "builtInMl"
	microsoftInsiderRiskManagement = "microsoftInsiderRiskManagement"
	microsoftSentinel = "microsoftSentinel"

