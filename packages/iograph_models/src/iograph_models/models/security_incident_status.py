from __future__ import annotations
from enum import Enum


class SecurityIncidentStatus(Enum):
	active = "active"
	resolved = "resolved"
	inProgress = "inProgress"
	redirected = "redirected"
	unknownFutureValue = "unknownFutureValue"
	awaitingAction = "awaitingAction"

