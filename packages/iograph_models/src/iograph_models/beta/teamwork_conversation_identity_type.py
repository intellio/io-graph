from __future__ import annotations
from enum import StrEnum


class TeamworkConversationIdentityType(StrEnum):
	team = "team"
	channel = "channel"
	chat = "chat"
	unknownFutureValue = "unknownFutureValue"

