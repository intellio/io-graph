from __future__ import annotations
from enum import StrEnum


class TeamsAppPublishingState(StrEnum):
	submitted = "submitted"
	rejected = "rejected"
	published = "published"
	unknownFutureValue = "unknownFutureValue"

