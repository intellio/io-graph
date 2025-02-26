from __future__ import annotations
from enum import Enum


class TeamsAppPublishingState(Enum):
	submitted = "submitted"
	rejected = "rejected"
	published = "published"
	unknownFutureValue = "unknownFutureValue"

