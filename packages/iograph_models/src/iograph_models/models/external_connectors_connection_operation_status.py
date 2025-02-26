from __future__ import annotations
from enum import Enum


class ExternalConnectorsConnectionOperationStatus(Enum):
	unspecified = "unspecified"
	inprogress = "inprogress"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

