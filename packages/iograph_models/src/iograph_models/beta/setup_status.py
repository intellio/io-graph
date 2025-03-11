from __future__ import annotations
from enum import StrEnum


class SetupStatus(StrEnum):
	unknown = "unknown"
	notRegisteredYet = "notRegisteredYet"
	registeredSetupNotStarted = "registeredSetupNotStarted"
	registeredSetupInProgress = "registeredSetupInProgress"
	registrationAndSetupCompleted = "registrationAndSetupCompleted"
	registrationFailed = "registrationFailed"
	registrationTimedOut = "registrationTimedOut"
	disabled = "disabled"

