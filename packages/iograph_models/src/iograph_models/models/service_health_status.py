from __future__ import annotations
from enum import StrEnum


class ServiceHealthStatus(StrEnum):
	serviceOperational = "serviceOperational"
	investigating = "investigating"
	restoringService = "restoringService"
	verifyingService = "verifyingService"
	serviceRestored = "serviceRestored"
	postIncidentReviewPublished = "postIncidentReviewPublished"
	serviceDegradation = "serviceDegradation"
	serviceInterruption = "serviceInterruption"
	extendedRecovery = "extendedRecovery"
	falsePositive = "falsePositive"
	investigationSuspended = "investigationSuspended"
	resolved = "resolved"
	mitigatedExternal = "mitigatedExternal"
	mitigated = "mitigated"
	resolvedExternal = "resolvedExternal"
	confirmed = "confirmed"
	reported = "reported"
	unknownFutureValue = "unknownFutureValue"

