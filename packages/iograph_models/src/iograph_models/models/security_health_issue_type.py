from __future__ import annotations
from enum import Enum


class SecurityHealthIssueType(Enum):
	sensor = "sensor"
	global_ = "global_"
	unknownFutureValue = "unknownFutureValue"

