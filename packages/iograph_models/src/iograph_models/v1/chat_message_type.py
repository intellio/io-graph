from __future__ import annotations
from enum import StrEnum


class ChatMessageType(StrEnum):
	message = "message"
	chatEvent = "chatEvent"
	typing = "typing"
	unknownFutureValue = "unknownFutureValue"
	systemEventMessage = "systemEventMessage"

