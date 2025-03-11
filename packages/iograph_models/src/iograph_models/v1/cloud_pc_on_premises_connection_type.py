from __future__ import annotations
from enum import StrEnum


class CloudPcOnPremisesConnectionType(StrEnum):
	hybridAzureADJoin = "hybridAzureADJoin"
	azureADJoin = "azureADJoin"
	unknownFutureValue = "unknownFutureValue"

