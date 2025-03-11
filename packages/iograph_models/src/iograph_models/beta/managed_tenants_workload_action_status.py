from __future__ import annotations
from enum import StrEnum


class ManagedTenantsWorkloadActionStatus(StrEnum):
	toAddress = "toAddress"
	completed = "completed"
	error = "error"
	timeOut = "timeOut"
	inProgress = "inProgress"
	unknownFutureValue = "unknownFutureValue"

