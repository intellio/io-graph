from __future__ import annotations
from enum import Enum


class SecurityBehaviorDuringRetentionPeriod(Enum):
	doNotRetain = "doNotRetain"
	retain = "retain"
	retainAsRecord = "retainAsRecord"
	retainAsRegulatoryRecord = "retainAsRegulatoryRecord"
	unknownFutureValue = "unknownFutureValue"

