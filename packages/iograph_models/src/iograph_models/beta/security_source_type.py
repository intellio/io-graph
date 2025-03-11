from __future__ import annotations
from enum import StrEnum


class SecuritySourceType(StrEnum):
	mailbox = "mailbox"
	site = "site"
	unknownFutureValue = "unknownFutureValue"

