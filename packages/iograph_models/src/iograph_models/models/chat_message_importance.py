from __future__ import annotations
from enum import Enum


class ChatMessageImportance(Enum):
	normal = "normal"
	high = "high"
	urgent = "urgent"
	unknownFutureValue = "unknownFutureValue"

