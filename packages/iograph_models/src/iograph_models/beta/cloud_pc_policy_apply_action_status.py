from __future__ import annotations
from enum import StrEnum


class CloudPcPolicyApplyActionStatus(StrEnum):
	processing = "processing"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

