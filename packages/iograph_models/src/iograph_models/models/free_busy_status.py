from __future__ import annotations
from enum import Enum


class FreeBusyStatus(Enum):
	unknown = "unknown"
	free = "free"
	tentative = "tentative"
	busy = "busy"
	oof = "oof"
	workingElsewhere = "workingElsewhere"

