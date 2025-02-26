from __future__ import annotations
from enum import Enum


class SecuritySensorType(Enum):
	adConnectIntegrated = "adConnectIntegrated"
	adcsIntegrated = "adcsIntegrated"
	adfsIntegrated = "adfsIntegrated"
	domainControllerIntegrated = "domainControllerIntegrated"
	domainControllerStandalone = "domainControllerStandalone"
	unknownFutureValue = "unknownFutureValue"

