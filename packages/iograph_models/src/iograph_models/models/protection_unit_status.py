from __future__ import annotations
from enum import StrEnum


class ProtectionUnitStatus(StrEnum):
	protectRequested = "protectRequested"
	protected = "protected"
	unprotectRequested = "unprotectRequested"
	unprotected = "unprotected"
	removeRequested = "removeRequested"
	unknownFutureValue = "unknownFutureValue"

