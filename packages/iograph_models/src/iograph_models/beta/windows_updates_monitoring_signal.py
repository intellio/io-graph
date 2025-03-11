from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesMonitoringSignal(StrEnum):
	rollback = "rollback"
	ineligible = "ineligible"
	unknownFutureValue = "unknownFutureValue"

