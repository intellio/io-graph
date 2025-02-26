from __future__ import annotations
from enum import Enum


class ProtectionUnitStatus(Enum):
	protectRequested = "protectRequested"
	protected = "protected"
	unprotectRequested = "unprotectRequested"
	unprotected = "unprotected"
	removeRequested = "removeRequested"
	unknownFutureValue = "unknownFutureValue"

