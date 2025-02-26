from __future__ import annotations
from enum import Enum


class CallRecordsModality(Enum):
	audio = "audio"
	video = "video"
	videoBasedScreenSharing = "videoBasedScreenSharing"
	data = "data"
	screenSharing = "screenSharing"
	unknownFutureValue = "unknownFutureValue"

