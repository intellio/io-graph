from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesCveSeverityLevel(StrEnum):
	critical = "critical"
	important = "important"
	moderate = "moderate"
	unknownFutureValue = "unknownFutureValue"

