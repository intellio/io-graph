from __future__ import annotations
from enum import StrEnum


class ZebraFotaDeploymentState(StrEnum):
	pendingCreation = "pendingCreation"
	createFailed = "createFailed"
	created = "created"
	inProgress = "inProgress"
	completed = "completed"
	pendingCancel = "pendingCancel"
	canceled = "canceled"
	unknownFutureValue = "unknownFutureValue"

