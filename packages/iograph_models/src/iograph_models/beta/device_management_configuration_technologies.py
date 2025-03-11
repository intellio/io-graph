from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationTechnologies(StrEnum):
	none = "none"
	mdm = "mdm"
	windows10XManagement = "windows10XManagement"
	configManager = "configManager"
	intuneManagementExtension = "intuneManagementExtension"
	thirdParty = "thirdParty"
	documentGateway = "documentGateway"
	appleRemoteManagement = "appleRemoteManagement"
	microsoftSense = "microsoftSense"
	exchangeOnline = "exchangeOnline"
	mobileApplicationManagement = "mobileApplicationManagement"
	linuxMdm = "linuxMdm"
	enrollment = "enrollment"
	endpointPrivilegeManagement = "endpointPrivilegeManagement"
	unknownFutureValue = "unknownFutureValue"
	windowsOsRecovery = "windowsOsRecovery"
	android = "android"

