from __future__ import annotations
from enum import StrEnum


class CloudPcPowerState(StrEnum):
	running = "running"
	poweredOff = "poweredOff"
	unknownFutureValue = "unknownFutureValue"

