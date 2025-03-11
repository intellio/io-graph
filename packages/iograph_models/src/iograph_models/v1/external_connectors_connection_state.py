from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsConnectionState(StrEnum):
	draft = "draft"
	ready = "ready"
	obsolete = "obsolete"
	limitExceeded = "limitExceeded"
	unknownFutureValue = "unknownFutureValue"

