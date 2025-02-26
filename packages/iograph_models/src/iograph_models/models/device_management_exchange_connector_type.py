from __future__ import annotations
from enum import Enum


class DeviceManagementExchangeConnectorType(Enum):
	onPremises = "onPremises"
	hosted = "hosted"
	serviceToService = "serviceToService"
	dedicated = "dedicated"
	unknownFutureValue = "unknownFutureValue"

