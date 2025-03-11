from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationAzureAdTrustType(StrEnum):
	none = "none"
	azureAdJoined = "azureAdJoined"
	addWorkAccount = "addWorkAccount"
	mdmOnly = "mdmOnly"

