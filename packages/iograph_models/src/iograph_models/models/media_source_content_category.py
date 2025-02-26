from __future__ import annotations
from enum import Enum


class MediaSourceContentCategory(Enum):
	meeting = "meeting"
	liveStream = "liveStream"
	presentation = "presentation"
	screenRecording = "screenRecording"
	story = "story"
	profile = "profile"
	chat = "chat"
	note = "note"
	comment = "comment"
	unknownFutureValue = "unknownFutureValue"

