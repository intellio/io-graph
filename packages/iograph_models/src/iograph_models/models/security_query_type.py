from __future__ import annotations
from enum import Enum


class SecurityQueryType(Enum):
	files = "files"
	messages = "messages"
	unknownFutureValue = "unknownFutureValue"

