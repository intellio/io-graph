from __future__ import annotations
from enum import StrEnum


class ManagedTenantsManagementActionStatus(StrEnum):
	toAddress = "toAddress"
	completed = "completed"
	error = "error"
	timeOut = "timeOut"
	inProgress = "inProgress"
	planned = "planned"
	resolvedBy3rdParty = "resolvedBy3rdParty"
	resolvedThroughAlternateMitigation = "resolvedThroughAlternateMitigation"
	riskAccepted = "riskAccepted"
	unknownFutureValue = "unknownFutureValue"

