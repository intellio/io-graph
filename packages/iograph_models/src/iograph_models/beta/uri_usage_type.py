from __future__ import annotations
from enum import StrEnum


class UriUsageType(StrEnum):
	redirectUri = "redirectUri"
	identifierUri = "identifierUri"
	loginUrl = "loginUrl"
	logoutUrl = "logoutUrl"
	unknownFutureValue = "unknownFutureValue"

