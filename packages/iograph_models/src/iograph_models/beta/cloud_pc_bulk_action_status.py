from __future__ import annotations
from enum import StrEnum


class CloudPcBulkActionStatus(StrEnum):
	pending = "pending"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

