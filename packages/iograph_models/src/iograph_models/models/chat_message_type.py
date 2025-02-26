from __future__ import annotations
from enum import Enum


class ChatMessageType(Enum):
	message = "message"
	chatEvent = "chatEvent"
	typing = "typing"
	unknownFutureValue = "unknownFutureValue"
	systemEventMessage = "systemEventMessage"

