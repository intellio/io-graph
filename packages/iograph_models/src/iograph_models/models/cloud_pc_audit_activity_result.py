from __future__ import annotations
from enum import StrEnum


class CloudPcAuditActivityResult(StrEnum):
	success = "success"
	clientError = "clientError"
	failure = "failure"
	timeout = "timeout"
	unknownFutureValue = "unknownFutureValue"

