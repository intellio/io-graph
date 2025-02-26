from __future__ import annotations
from enum import Enum


class BackupServiceConsumer(Enum):
	unknown = "unknown"
	firstparty = "firstparty"
	thirdparty = "thirdparty"
	unknownFutureValue = "unknownFutureValue"

