from __future__ import annotations
from enum import StrEnum


class ArtifactRestoreStatus(StrEnum):
	added = "added"
	scheduling = "scheduling"
	scheduled = "scheduled"
	inProgress = "inProgress"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

