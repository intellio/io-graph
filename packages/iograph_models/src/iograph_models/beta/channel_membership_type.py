from __future__ import annotations
from enum import StrEnum


class ChannelMembershipType(StrEnum):
	standard = "standard"
	private = "private"
	unknownFutureValue = "unknownFutureValue"
	shared = "shared"

