from __future__ import annotations
from enum import StrEnum


class LifecycleEventType(StrEnum):
	missed = "missed"
	subscriptionRemoved = "subscriptionRemoved"
	reauthorizationRequired = "reauthorizationRequired"

