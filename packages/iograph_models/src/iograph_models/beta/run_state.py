from __future__ import annotations
from enum import StrEnum


class RunState(StrEnum):
	unknown = "unknown"
	success = "success"
	fail = "fail"
	scriptError = "scriptError"
	pending = "pending"
	notApplicable = "notApplicable"

