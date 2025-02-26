from __future__ import annotations
from enum import Enum


class SecurityPurgeAreas(Enum):
	mailboxes = "mailboxes"
	teamsMessages = "teamsMessages"
	unknownFutureValue = "unknownFutureValue"

