from __future__ import annotations
from enum import StrEnum


class VppTokenSyncStatus(StrEnum):
	none = "none"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"

