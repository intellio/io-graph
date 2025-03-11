from __future__ import annotations
from enum import StrEnum


class MailboxType(StrEnum):
	unknown = "unknown"
	user = "user"
	shared = "shared"
	unknownFutureValue = "unknownFutureValue"

