from __future__ import annotations
from enum import Enum


class ExternalConnectorsAccessType(Enum):
	grant = "grant"
	deny = "deny"
	unknownFutureValue = "unknownFutureValue"

