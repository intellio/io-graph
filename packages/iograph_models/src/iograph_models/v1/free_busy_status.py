from __future__ import annotations
from enum import StrEnum


class FreeBusyStatus(StrEnum):
	unknown = "unknown"
	free = "free"
	tentative = "tentative"
	busy = "busy"
	oof = "oof"
	workingElsewhere = "workingElsewhere"

