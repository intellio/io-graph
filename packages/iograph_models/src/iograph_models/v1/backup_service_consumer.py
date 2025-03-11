from __future__ import annotations
from enum import StrEnum


class BackupServiceConsumer(StrEnum):
	unknown = "unknown"
	firstparty = "firstparty"
	thirdparty = "thirdparty"
	unknownFutureValue = "unknownFutureValue"

