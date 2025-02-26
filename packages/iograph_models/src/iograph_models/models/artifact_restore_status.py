from __future__ import annotations
from enum import Enum


class ArtifactRestoreStatus(Enum):
	added = "added"
	scheduling = "scheduling"
	scheduled = "scheduled"
	inProgress = "inProgress"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

