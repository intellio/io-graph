from __future__ import annotations
from enum import Enum


class CallRecordingStatus(Enum):
	success = "success"
	failure = "failure"
	initial = "initial"
	chunkFinished = "chunkFinished"
	unknownFutureValue = "unknownFutureValue"

