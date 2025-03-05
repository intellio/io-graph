from __future__ import annotations
from enum import StrEnum


class FollowupFlagStatus(StrEnum):
	notFlagged = "notFlagged"
	complete = "complete"
	flagged = "flagged"

