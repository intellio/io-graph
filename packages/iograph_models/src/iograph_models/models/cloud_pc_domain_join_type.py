from __future__ import annotations
from enum import Enum


class CloudPcDomainJoinType(Enum):
	azureADJoin = "azureADJoin"
	hybridAzureADJoin = "hybridAzureADJoin"
	unknownFutureValue = "unknownFutureValue"

