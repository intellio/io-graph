from __future__ import annotations
from enum import StrEnum


class ChatType(StrEnum):
	oneOnOne = "oneOnOne"
	group = "group"
	meeting = "meeting"
	unknownFutureValue = "unknownFutureValue"

