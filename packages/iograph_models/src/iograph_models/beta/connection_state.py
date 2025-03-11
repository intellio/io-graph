from __future__ import annotations
from enum import StrEnum


class ConnectionState(StrEnum):
	draft = "draft"
	ready = "ready"
	obsolete = "obsolete"
	limitExceeded = "limitExceeded"
	unknownFutureValue = "unknownFutureValue"

