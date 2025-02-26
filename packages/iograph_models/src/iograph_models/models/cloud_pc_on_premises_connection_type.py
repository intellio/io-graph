from __future__ import annotations
from enum import Enum


class CloudPcOnPremisesConnectionType(Enum):
	hybridAzureADJoin = "hybridAzureADJoin"
	azureADJoin = "azureADJoin"
	unknownFutureValue = "unknownFutureValue"

