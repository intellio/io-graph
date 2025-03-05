from __future__ import annotations
from enum import StrEnum


class WindowsDeliveryOptimizationMode(StrEnum):
	userDefined = "userDefined"
	httpOnly = "httpOnly"
	httpWithPeeringNat = "httpWithPeeringNat"
	httpWithPeeringPrivateGroup = "httpWithPeeringPrivateGroup"
	httpWithInternetPeering = "httpWithInternetPeering"
	simpleDownload = "simpleDownload"
	bypassMode = "bypassMode"

