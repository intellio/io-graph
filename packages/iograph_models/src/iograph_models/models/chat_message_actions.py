from __future__ import annotations
from enum import StrEnum


class ChatMessageActions(StrEnum):
	reactionAdded = "reactionAdded"
	reactionRemoved = "reactionRemoved"
	actionUndefined = "actionUndefined"
	unknownFutureValue = "unknownFutureValue"

