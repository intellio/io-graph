from __future__ import annotations
from enum import Enum


class CallRecordsFailureStage(Enum):
	unknown = "unknown"
	callSetup = "callSetup"
	midcall = "midcall"
	unknownFutureValue = "unknownFutureValue"

