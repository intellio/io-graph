from __future__ import annotations
from enum import Enum


class TeamworkConversationIdentityType(Enum):
	team = "team"
	channel = "channel"
	chat = "chat"
	unknownFutureValue = "unknownFutureValue"

