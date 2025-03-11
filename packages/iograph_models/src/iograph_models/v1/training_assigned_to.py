from __future__ import annotations
from enum import StrEnum


class TrainingAssignedTo(StrEnum):
	none = "none"
	allUsers = "allUsers"
	clickedPayload = "clickedPayload"
	compromised = "compromised"
	reportedPhish = "reportedPhish"
	readButNotClicked = "readButNotClicked"
	didNothing = "didNothing"
	unknownFutureValue = "unknownFutureValue"

