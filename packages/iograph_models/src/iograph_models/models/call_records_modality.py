from __future__ import annotations
from enum import StrEnum


class CallRecordsModality(StrEnum):
	audio = "audio"
	video = "video"
	videoBasedScreenSharing = "videoBasedScreenSharing"
	data = "data"
	screenSharing = "screenSharing"
	unknownFutureValue = "unknownFutureValue"

