from __future__ import annotations
from enum import Enum


class SecurityRetentionTrigger(Enum):
	dateLabeled = "dateLabeled"
	dateCreated = "dateCreated"
	dateModified = "dateModified"
	dateOfEvent = "dateOfEvent"
	unknownFutureValue = "unknownFutureValue"

