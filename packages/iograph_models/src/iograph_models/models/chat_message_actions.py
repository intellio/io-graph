from __future__ import annotations
from enum import Enum


class ChatMessageActions(Enum):
	reactionAdded = "reactionAdded"
	reactionRemoved = "reactionRemoved"
	actionUndefined = "actionUndefined"
	unknownFutureValue = "unknownFutureValue"

