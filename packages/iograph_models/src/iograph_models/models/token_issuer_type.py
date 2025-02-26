from __future__ import annotations
from enum import Enum


class TokenIssuerType(Enum):
	AzureAD = "AzureAD"
	ADFederationServices = "ADFederationServices"
	UnknownFutureValue = "UnknownFutureValue"
	AzureADBackupAuth = "AzureADBackupAuth"
	ADFederationServicesMFAAdapter = "ADFederationServicesMFAAdapter"
	NPSExtension = "NPSExtension"

