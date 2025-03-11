from __future__ import annotations
from enum import StrEnum


class ConditionalAccessConditions(StrEnum):
	none = "none"
	application = "application"
	users = "users"
	devicePlatform = "devicePlatform"
	location = "location"
	clientType = "clientType"
	signInRisk = "signInRisk"
	userRisk = "userRisk"
	time = "time"
	deviceState = "deviceState"
	client = "client"
	ipAddressSeenByAzureAD = "ipAddressSeenByAzureAD"
	ipAddressSeenByResourceProvider = "ipAddressSeenByResourceProvider"
	unknownFutureValue = "unknownFutureValue"
	servicePrincipals = "servicePrincipals"
	servicePrincipalRisk = "servicePrincipalRisk"
	authenticationFlows = "authenticationFlows"
	insiderRisk = "insiderRisk"

