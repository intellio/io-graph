from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsAccessType(StrEnum):
	grant = "grant"
	deny = "deny"
	unknownFutureValue = "unknownFutureValue"

