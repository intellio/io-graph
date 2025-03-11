from __future__ import annotations
from enum import StrEnum


class TokenIssuerType(StrEnum):
	AzureAD = "AzureAD"
	ADFederationServices = "ADFederationServices"
	UnknownFutureValue = "UnknownFutureValue"
	AzureADBackupAuth = "AzureADBackupAuth"
	ADFederationServicesMFAAdapter = "ADFederationServicesMFAAdapter"
	NPSExtension = "NPSExtension"

