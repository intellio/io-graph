from __future__ import annotations
from enum import StrEnum


class ConditionalAccessWhatIfReasons(StrEnum):
	notSet = "notSet"
	notEnoughInformation = "notEnoughInformation"
	invalidCondition = "invalidCondition"
	users = "users"
	workloadIdentities = "workloadIdentities"
	application = "application"
	userActions = "userActions"
	authenticationContext = "authenticationContext"
	devicePlatform = "devicePlatform"
	devices = "devices"
	clientApps = "clientApps"
	location = "location"
	signInRisk = "signInRisk"
	emptyPolicy = "emptyPolicy"
	invalidPolicy = "invalidPolicy"
	policyNotEnabled = "policyNotEnabled"
	userRisk = "userRisk"
	time = "time"
	insiderRisk = "insiderRisk"
	authenticationFlow = "authenticationFlow"
	unknownFutureValue = "unknownFutureValue"

