from __future__ import annotations
from enum import StrEnum


class ChannelLayoutType(StrEnum):
	post = "post"
	chat = "chat"
	unknownFutureValue = "unknownFutureValue"

