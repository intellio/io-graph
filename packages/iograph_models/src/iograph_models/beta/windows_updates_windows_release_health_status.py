from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesWindowsReleaseHealthStatus(StrEnum):
	resolved = "resolved"
	mitigatedExternal = "mitigatedExternal"
	mitigated = "mitigated"
	resolvedExternal = "resolvedExternal"
	confirmed = "confirmed"
	reported = "reported"
	investigating = "investigating"
	unknownFutureValue = "unknownFutureValue"

