from __future__ import annotations
from enum import StrEnum


class CallRecordsMediaStreamDirection(StrEnum):
	callerToCallee = "callerToCallee"
	calleeToCaller = "calleeToCaller"

