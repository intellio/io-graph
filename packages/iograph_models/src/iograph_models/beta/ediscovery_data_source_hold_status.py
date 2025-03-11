from __future__ import annotations
from enum import StrEnum


class EdiscoveryDataSourceHoldStatus(StrEnum):
	notApplied = "notApplied"
	applied = "applied"
	applying = "applying"
	removing = "removing"
	partial = "partial"
	unknownFutureValue = "unknownFutureValue"

