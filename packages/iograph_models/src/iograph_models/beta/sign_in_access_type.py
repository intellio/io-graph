from __future__ import annotations
from enum import StrEnum


class SignInAccessType(StrEnum):
	none = "none"
	b2bCollaboration = "b2bCollaboration"
	b2bDirectConnect = "b2bDirectConnect"
	microsoftSupport = "microsoftSupport"
	serviceProvider = "serviceProvider"
	unknownFutureValue = "unknownFutureValue"
	passthrough = "passthrough"

