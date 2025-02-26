from __future__ import annotations
from enum import Enum


class ExternalConnectorsIdentityType(Enum):
	user = "user"
	group = "group"
	externalGroup = "externalGroup"
	unknownFutureValue = "unknownFutureValue"

