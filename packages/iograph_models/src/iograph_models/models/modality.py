from __future__ import annotations
from enum import Enum


class Modality(Enum):
	audio = "audio"
	video = "video"
	videoBasedScreenSharing = "videoBasedScreenSharing"
	data = "data"
	unknownFutureValue = "unknownFutureValue"

