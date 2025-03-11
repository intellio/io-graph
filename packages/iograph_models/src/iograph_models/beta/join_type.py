from __future__ import annotations
from enum import StrEnum


class JoinType(StrEnum):
	unknown = "unknown"
	azureADJoined = "azureADJoined"
	azureADRegistered = "azureADRegistered"
	hybridAzureADJoined = "hybridAzureADJoined"

