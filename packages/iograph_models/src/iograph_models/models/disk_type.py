from __future__ import annotations
from enum import StrEnum


class DiskType(StrEnum):
	unknown = "unknown"
	hdd = "hdd"
	ssd = "ssd"
	unknownFutureValue = "unknownFutureValue"

