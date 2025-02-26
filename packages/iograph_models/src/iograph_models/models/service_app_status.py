from __future__ import annotations
from enum import Enum


class ServiceAppStatus(Enum):
	inactive = "inactive"
	active = "active"
	pendingActive = "pendingActive"
	pendingInactive = "pendingInactive"
	unknownFutureValue = "unknownFutureValue"

