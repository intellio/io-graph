from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsConnectionOperationStatus(StrEnum):
	unspecified = "unspecified"
	inprogress = "inprogress"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

