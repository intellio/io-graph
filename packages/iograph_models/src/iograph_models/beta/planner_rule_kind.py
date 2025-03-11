from __future__ import annotations
from enum import StrEnum


class PlannerRuleKind(StrEnum):
	taskRule = "taskRule"
	bucketRule = "bucketRule"
	planRule = "planRule"
	unknownFutureValue = "unknownFutureValue"

