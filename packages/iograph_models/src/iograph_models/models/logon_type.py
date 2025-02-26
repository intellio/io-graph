from __future__ import annotations
from enum import Enum


class LogonType(Enum):
	unknown = "unknown"
	interactive = "interactive"
	remoteInteractive = "remoteInteractive"
	network = "network"
	batch = "batch"
	service = "service"
	unknownFutureValue = "unknownFutureValue"

