from __future__ import annotations
from enum import Enum


class SecuritySourceType(Enum):
	mailbox = "mailbox"
	site = "site"
	unknownFutureValue = "unknownFutureValue"

