from __future__ import annotations
from enum import StrEnum


class CalendarRoleType(StrEnum):
	none = "none"
	freeBusyRead = "freeBusyRead"
	limitedRead = "limitedRead"
	read = "read"
	write = "write"
	delegateWithoutPrivateEventAccess = "delegateWithoutPrivateEventAccess"
	delegateWithPrivateEventAccess = "delegateWithPrivateEventAccess"
	custom = "custom"

