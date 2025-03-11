from __future__ import annotations
from enum import StrEnum


class AssociatedAssignmentPayloadType(StrEnum):
	unknown = "unknown"
	deviceConfigurationAndCompliance = "deviceConfigurationAndCompliance"
	application = "application"
	androidEnterpriseApp = "androidEnterpriseApp"
	enrollmentConfiguration = "enrollmentConfiguration"
	groupPolicyConfiguration = "groupPolicyConfiguration"
	zeroTouchDeploymentDeviceConfigProfile = "zeroTouchDeploymentDeviceConfigProfile"
	androidEnterpriseConfiguration = "androidEnterpriseConfiguration"
	deviceFirmwareConfigurationInterfacePolicy = "deviceFirmwareConfigurationInterfacePolicy"
	resourceAccessPolicy = "resourceAccessPolicy"
	win32app = "win32app"
	deviceManagmentConfigurationAndCompliancePolicy = "deviceManagmentConfigurationAndCompliancePolicy"

