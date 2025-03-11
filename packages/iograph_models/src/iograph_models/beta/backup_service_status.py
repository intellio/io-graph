from __future__ import annotations
from enum import StrEnum


class BackupServiceStatus(StrEnum):
	disabled = "disabled"
	enabled = "enabled"
	protectionChangeLocked = "protectionChangeLocked"
	restoreLocked = "restoreLocked"
	unknownFutureValue = "unknownFutureValue"

