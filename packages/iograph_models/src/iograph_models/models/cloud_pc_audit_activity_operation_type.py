from __future__ import annotations
from enum import Enum


class CloudPcAuditActivityOperationType(Enum):
	create = "create"
	delete = "delete"
	patch = "patch"
	unknownFutureValue = "unknownFutureValue"

