from __future__ import annotations
from enum import StrEnum


class SecurityIncidentStatus(StrEnum):
	active = "active"
	resolved = "resolved"
	inProgress = "inProgress"
	redirected = "redirected"
	unknownFutureValue = "unknownFutureValue"
	awaitingAction = "awaitingAction"

