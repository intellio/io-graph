from __future__ import annotations
from enum import StrEnum


class ZebraFotaUpdateType(StrEnum):
	custom = "custom"
	latest = "latest"
	auto = "auto"
	unknownFutureValue = "unknownFutureValue"

