from __future__ import annotations
from enum import StrEnum


class SecurityRetentionTrigger(StrEnum):
	dateLabeled = "dateLabeled"
	dateCreated = "dateCreated"
	dateModified = "dateModified"
	dateOfEvent = "dateOfEvent"
	unknownFutureValue = "unknownFutureValue"

