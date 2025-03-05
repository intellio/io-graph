from __future__ import annotations
from enum import StrEnum


class SecurityDeploymentStatus(StrEnum):
	upToDate = "upToDate"
	outdated = "outdated"
	updating = "updating"
	updateFailed = "updateFailed"
	notConfigured = "notConfigured"
	unreachable = "unreachable"
	disconnected = "disconnected"
	startFailure = "startFailure"
	syncing = "syncing"
	unknownFutureValue = "unknownFutureValue"

