from __future__ import annotations
from enum import Enum


class CalendarRoleType(Enum):
	none = "none"
	freeBusyRead = "freeBusyRead"
	limitedRead = "limitedRead"
	read = "read"
	write = "write"
	delegateWithoutPrivateEventAccess = "delegateWithoutPrivateEventAccess"
	delegateWithPrivateEventAccess = "delegateWithPrivateEventAccess"
	custom = "custom"

