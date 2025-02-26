from __future__ import annotations
from enum import Enum


class FollowupFlagStatus(Enum):
	notFlagged = "notFlagged"
	complete = "complete"
	flagged = "flagged"

