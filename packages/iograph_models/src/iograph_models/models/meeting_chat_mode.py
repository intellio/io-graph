from __future__ import annotations
from enum import Enum


class MeetingChatMode(Enum):
	enabled = "enabled"
	disabled = "disabled"
	limited = "limited"
	unknownFutureValue = "unknownFutureValue"

