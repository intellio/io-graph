from __future__ import annotations
from enum import Enum


class VppTokenSyncStatus(Enum):
	none = "none"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"

