from __future__ import annotations
from enum import StrEnum


class Modality(StrEnum):
	unknown = "unknown"
	audio = "audio"
	video = "video"
	videoBasedScreenSharing = "videoBasedScreenSharing"
	data = "data"
	unknownFutureValue = "unknownFutureValue"

