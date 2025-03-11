from __future__ import annotations
from enum import StrEnum


class SecurityPurgeAreas(StrEnum):
	mailboxes = "mailboxes"
	teamsMessages = "teamsMessages"
	unknownFutureValue = "unknownFutureValue"

