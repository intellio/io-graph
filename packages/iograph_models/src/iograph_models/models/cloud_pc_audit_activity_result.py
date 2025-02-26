from __future__ import annotations
from enum import Enum


class CloudPcAuditActivityResult(Enum):
	success = "success"
	clientError = "clientError"
	failure = "failure"
	timeout = "timeout"
	unknownFutureValue = "unknownFutureValue"

