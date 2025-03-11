from __future__ import annotations
from enum import StrEnum


class SecurityTenantAllowBlockListEntryType(StrEnum):
	url = "url"
	fileHash = "fileHash"
	sender = "sender"
	recipient = "recipient"
	unknownFutureValue = "unknownFutureValue"

