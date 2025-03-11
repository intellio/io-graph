from __future__ import annotations
from enum import StrEnum


class LogonType(StrEnum):
	unknown = "unknown"
	interactive = "interactive"
	remoteInteractive = "remoteInteractive"
	network = "network"
	batch = "batch"
	service = "service"
	unknownFutureValue = "unknownFutureValue"

