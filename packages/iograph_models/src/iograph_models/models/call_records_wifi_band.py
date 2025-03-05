from __future__ import annotations
from enum import StrEnum


class CallRecordsWifiBand(StrEnum):
	unknown = "unknown"
	frequency24GHz = "frequency24GHz"
	frequency50GHz = "frequency50GHz"
	frequency60GHz = "frequency60GHz"
	unknownFutureValue = "unknownFutureValue"

