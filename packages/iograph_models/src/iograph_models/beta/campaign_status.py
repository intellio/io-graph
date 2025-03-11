from __future__ import annotations
from enum import StrEnum


class CampaignStatus(StrEnum):
	unknown = "unknown"
	draft = "draft"
	inProgress = "inProgress"
	scheduled = "scheduled"
	completed = "completed"
	failed = "failed"
	cancelled = "cancelled"
	excluded = "excluded"
	deleted = "deleted"
	unknownFutureValue = "unknownFutureValue"

