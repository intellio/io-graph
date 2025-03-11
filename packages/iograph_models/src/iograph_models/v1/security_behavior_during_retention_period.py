from __future__ import annotations
from enum import StrEnum


class SecurityBehaviorDuringRetentionPeriod(StrEnum):
	doNotRetain = "doNotRetain"
	retain = "retain"
	retainAsRecord = "retainAsRecord"
	retainAsRegulatoryRecord = "retainAsRegulatoryRecord"
	unknownFutureValue = "unknownFutureValue"

