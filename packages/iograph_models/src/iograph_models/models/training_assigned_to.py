from __future__ import annotations
from enum import Enum


class TrainingAssignedTo(Enum):
	none = "none"
	allUsers = "allUsers"
	clickedPayload = "clickedPayload"
	compromised = "compromised"
	reportedPhish = "reportedPhish"
	readButNotClicked = "readButNotClicked"
	didNothing = "didNothing"
	unknownFutureValue = "unknownFutureValue"

