from __future__ import annotations
from enum import Enum


class ExternalConnectorsConnectionState(Enum):
	draft = "draft"
	ready = "ready"
	obsolete = "obsolete"
	limitExceeded = "limitExceeded"
	unknownFutureValue = "unknownFutureValue"

