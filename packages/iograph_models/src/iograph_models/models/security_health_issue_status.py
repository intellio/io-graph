from __future__ import annotations
from enum import StrEnum


class SecurityHealthIssueStatus(StrEnum):
	open = "open"
	closed = "closed"
	suppressed = "suppressed"
	unknownFutureValue = "unknownFutureValue"

