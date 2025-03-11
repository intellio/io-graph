from __future__ import annotations
from enum import StrEnum


class MobileAppPublishingState(StrEnum):
	notPublished = "notPublished"
	processing = "processing"
	published = "published"

