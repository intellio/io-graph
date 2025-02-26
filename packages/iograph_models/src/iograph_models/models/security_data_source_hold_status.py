from __future__ import annotations
from enum import Enum


class SecurityDataSourceHoldStatus(Enum):
	notApplied = "notApplied"
	applied = "applied"
	applying = "applying"
	removing = "removing"
	partial = "partial"
	unknownFutureValue = "unknownFutureValue"

