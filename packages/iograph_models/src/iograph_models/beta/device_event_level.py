from __future__ import annotations
from enum import StrEnum


class DeviceEventLevel(StrEnum):
	none = "none"
	verbose = "verbose"
	information = "information"
	warning = "warning"
	error = "error"
	critical = "critical"
	unknownFutureValue = "unknownFutureValue"

