from __future__ import annotations
from enum import StrEnum


class DeviceManagementTemplateType(StrEnum):
	securityBaseline = "securityBaseline"
	specializedDevices = "specializedDevices"
	advancedThreatProtectionSecurityBaseline = "advancedThreatProtectionSecurityBaseline"
	deviceConfiguration = "deviceConfiguration"
	custom = "custom"
	securityTemplate = "securityTemplate"
	microsoftEdgeSecurityBaseline = "microsoftEdgeSecurityBaseline"
	microsoftOffice365ProPlusSecurityBaseline = "microsoftOffice365ProPlusSecurityBaseline"
	deviceCompliance = "deviceCompliance"
	deviceConfigurationForOffice365 = "deviceConfigurationForOffice365"
	cloudPC = "cloudPC"
	firewallSharedSettings = "firewallSharedSettings"

