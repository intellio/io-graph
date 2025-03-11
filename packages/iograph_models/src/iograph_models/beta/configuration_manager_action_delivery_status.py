from __future__ import annotations
from enum import StrEnum


class ConfigurationManagerActionDeliveryStatus(StrEnum):
	unknown = "unknown"
	pendingDelivery = "pendingDelivery"
	deliveredToConnectorService = "deliveredToConnectorService"
	failedToDeliverToConnectorService = "failedToDeliverToConnectorService"
	deliveredToOnPremisesServer = "deliveredToOnPremisesServer"

