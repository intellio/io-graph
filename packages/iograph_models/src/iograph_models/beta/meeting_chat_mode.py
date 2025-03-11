from __future__ import annotations
from enum import StrEnum


class MeetingChatMode(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	limited = "limited"
	unknownFutureValue = "unknownFutureValue"

