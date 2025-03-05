from __future__ import annotations
from enum import StrEnum


class SecurityQueryType(StrEnum):
	files = "files"
	messages = "messages"
	unknownFutureValue = "unknownFutureValue"

