from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesQualityUpdateClassification(StrEnum):
	all = "all"
	security = "security"
	nonSecurity = "nonSecurity"
	unknownFutureValue = "unknownFutureValue"

