from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotProfileAssignmentStatus(StrEnum):
	unknown = "unknown"
	assignedInSync = "assignedInSync"
	assignedOutOfSync = "assignedOutOfSync"
	assignedUnkownSyncState = "assignedUnkownSyncState"
	notAssigned = "notAssigned"
	pending = "pending"
	failed = "failed"

