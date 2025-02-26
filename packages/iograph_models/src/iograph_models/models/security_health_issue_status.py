from __future__ import annotations
from enum import Enum


class SecurityHealthIssueStatus(Enum):
	open = "open"
	closed = "closed"
	suppressed = "suppressed"
	unknownFutureValue = "unknownFutureValue"

