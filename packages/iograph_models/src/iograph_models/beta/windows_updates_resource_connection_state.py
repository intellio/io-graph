from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesResourceConnectionState(StrEnum):
	connected = "connected"
	notAuthorized = "notAuthorized"
	notFound = "notFound"
	unknownFutureValue = "unknownFutureValue"

