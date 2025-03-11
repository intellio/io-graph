from __future__ import annotations
from enum import StrEnum


class DeviceManagementExchangeConnectorType(StrEnum):
	onPremises = "onPremises"
	hosted = "hosted"
	serviceToService = "serviceToService"
	dedicated = "dedicated"
	unknownFutureValue = "unknownFutureValue"

