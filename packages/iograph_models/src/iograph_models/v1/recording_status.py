from __future__ import annotations
from enum import StrEnum


class RecordingStatus(StrEnum):
	unknown = "unknown"
	notRecording = "notRecording"
	recording = "recording"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

