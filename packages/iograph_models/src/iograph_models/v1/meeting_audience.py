from __future__ import annotations
from enum import StrEnum


class MeetingAudience(StrEnum):
	everyone = "everyone"
	organization = "organization"
	unknownFutureValue = "unknownFutureValue"

