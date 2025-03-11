from __future__ import annotations
from enum import StrEnum


class CallRecordsFailureStage(StrEnum):
	unknown = "unknown"
	callSetup = "callSetup"
	midcall = "midcall"
	unknownFutureValue = "unknownFutureValue"

