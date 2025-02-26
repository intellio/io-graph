from __future__ import annotations
from enum import Enum


class LifecycleEventType(Enum):
	missed = "missed"
	subscriptionRemoved = "subscriptionRemoved"
	reauthorizationRequired = "reauthorizationRequired"

