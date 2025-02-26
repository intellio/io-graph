from __future__ import annotations
from enum import Enum


class BackupServiceStatus(Enum):
	disabled = "disabled"
	enabled = "enabled"
	protectionChangeLocked = "protectionChangeLocked"
	restoreLocked = "restoreLocked"
	unknownFutureValue = "unknownFutureValue"

