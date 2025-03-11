from __future__ import annotations
from enum import StrEnum


class CloudPcAuditActivityOperationType(StrEnum):
	create = "create"
	delete = "delete"
	patch = "patch"
	unknownFutureValue = "unknownFutureValue"

