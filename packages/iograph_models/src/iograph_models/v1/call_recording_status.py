from __future__ import annotations
from enum import StrEnum


class CallRecordingStatus(StrEnum):
	success = "success"
	failure = "failure"
	initial = "initial"
	chunkFinished = "chunkFinished"
	unknownFutureValue = "unknownFutureValue"

