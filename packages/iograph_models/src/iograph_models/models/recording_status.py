from __future__ import annotations
from enum import Enum


class RecordingStatus(Enum):
	unknown = "unknown"
	notRecording = "notRecording"
	recording = "recording"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

