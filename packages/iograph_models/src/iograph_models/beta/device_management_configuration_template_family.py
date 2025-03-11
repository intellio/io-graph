from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationTemplateFamily(StrEnum):
	none = "none"
	endpointSecurityAntivirus = "endpointSecurityAntivirus"
	endpointSecurityDiskEncryption = "endpointSecurityDiskEncryption"
	endpointSecurityFirewall = "endpointSecurityFirewall"
	endpointSecurityEndpointDetectionAndResponse = "endpointSecurityEndpointDetectionAndResponse"
	endpointSecurityAttackSurfaceReduction = "endpointSecurityAttackSurfaceReduction"
	endpointSecurityAccountProtection = "endpointSecurityAccountProtection"
	endpointSecurityApplicationControl = "endpointSecurityApplicationControl"
	endpointSecurityEndpointPrivilegeManagement = "endpointSecurityEndpointPrivilegeManagement"
	enrollmentConfiguration = "enrollmentConfiguration"
	appQuietTime = "appQuietTime"
	baseline = "baseline"
	unknownFutureValue = "unknownFutureValue"
	deviceConfigurationScripts = "deviceConfigurationScripts"
	deviceConfigurationPolicies = "deviceConfigurationPolicies"
	windowsOsRecoveryPolicies = "windowsOsRecoveryPolicies"
	companyPortal = "companyPortal"

