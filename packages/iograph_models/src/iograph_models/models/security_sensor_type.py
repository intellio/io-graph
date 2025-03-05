from __future__ import annotations
from enum import StrEnum


class SecuritySensorType(StrEnum):
	adConnectIntegrated = "adConnectIntegrated"
	adcsIntegrated = "adcsIntegrated"
	adfsIntegrated = "adfsIntegrated"
	domainControllerIntegrated = "domainControllerIntegrated"
	domainControllerStandalone = "domainControllerStandalone"
	unknownFutureValue = "unknownFutureValue"

