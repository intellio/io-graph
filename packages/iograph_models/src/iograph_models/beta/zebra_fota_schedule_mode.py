from __future__ import annotations
from enum import StrEnum


class ZebraFotaScheduleMode(StrEnum):
	installNow = "installNow"
	scheduled = "scheduled"
	unknownFutureValue = "unknownFutureValue"

