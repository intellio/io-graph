from __future__ import annotations
from enum import StrEnum


class CloudPcDomainJoinType(StrEnum):
	azureADJoin = "azureADJoin"
	hybridAzureADJoin = "hybridAzureADJoin"
	unknownFutureValue = "unknownFutureValue"

