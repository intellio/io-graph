from __future__ import annotations
from enum import StrEnum


class ManagementAgentType(StrEnum):
	eas = "eas"
	mdm = "mdm"
	easMdm = "easMdm"
	intuneClient = "intuneClient"
	easIntuneClient = "easIntuneClient"
	configurationManagerClient = "configurationManagerClient"
	configurationManagerClientMdm = "configurationManagerClientMdm"
	configurationManagerClientMdmEas = "configurationManagerClientMdmEas"
	unknown = "unknown"
	jamf = "jamf"
	googleCloudDevicePolicyController = "googleCloudDevicePolicyController"
	microsoft365ManagedMdm = "microsoft365ManagedMdm"
	msSense = "msSense"

