from __future__ import annotations
from enum import Enum


class ChatType(Enum):
	oneOnOne = "oneOnOne"
	group = "group"
	meeting = "meeting"
	unknownFutureValue = "unknownFutureValue"

