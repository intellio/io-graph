from __future__ import annotations
from enum import Enum


class WindowsDeliveryOptimizationMode(Enum):
	userDefined = "userDefined"
	httpOnly = "httpOnly"
	httpWithPeeringNat = "httpWithPeeringNat"
	httpWithPeeringPrivateGroup = "httpWithPeeringPrivateGroup"
	httpWithInternetPeering = "httpWithInternetPeering"
	simpleDownload = "simpleDownload"
	bypassMode = "bypassMode"

