from __future__ import annotations
from enum import StrEnum


class DeviceManagementSubscriptions(StrEnum):
	none = "none"
	intune = "intune"
	office365 = "office365"
	intunePremium = "intunePremium"
	intune_EDU = "intune_EDU"
	intune_SMB = "intune_SMB"

