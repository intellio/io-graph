from __future__ import annotations
from enum import StrEnum


class ServiceAppStatus(StrEnum):
	inactive = "inactive"
	active = "active"
	pendingActive = "pendingActive"
	pendingInactive = "pendingInactive"
	unknownFutureValue = "unknownFutureValue"

