from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsIdentityType(StrEnum):
	user = "user"
	group = "group"
	externalGroup = "externalGroup"
	unknownFutureValue = "unknownFutureValue"

