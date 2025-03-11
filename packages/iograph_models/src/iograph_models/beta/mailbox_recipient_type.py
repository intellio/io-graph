from __future__ import annotations
from enum import StrEnum


class MailboxRecipientType(StrEnum):
	unknown = "unknown"
	user = "user"
	linked = "linked"
	shared = "shared"
	room = "room"
	equipment = "equipment"
	others = "others"

