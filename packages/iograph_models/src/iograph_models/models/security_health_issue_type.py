from __future__ import annotations
from enum import StrEnum


class SecurityHealthIssueType(StrEnum):
	sensor = "sensor"
	global_ = "global_"
	unknownFutureValue = "unknownFutureValue"

