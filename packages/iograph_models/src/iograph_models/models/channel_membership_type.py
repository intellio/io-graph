from __future__ import annotations
from enum import Enum


class ChannelMembershipType(Enum):
	standard = "standard"
	private = "private"
	unknownFutureValue = "unknownFutureValue"
	shared = "shared"

