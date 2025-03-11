from __future__ import annotations
from enum import StrEnum


class EmailSyncSchedule(StrEnum):
	userDefined = "userDefined"
	asMessagesArrive = "asMessagesArrive"
	manual = "manual"
	fifteenMinutes = "fifteenMinutes"
	thirtyMinutes = "thirtyMinutes"
	sixtyMinutes = "sixtyMinutes"
	basedOnMyUsage = "basedOnMyUsage"

