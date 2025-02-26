from __future__ import annotations
from enum import Enum


class CallRecordsMediaStreamDirection(Enum):
	callerToCallee = "callerToCallee"
	calleeToCaller = "calleeToCaller"

