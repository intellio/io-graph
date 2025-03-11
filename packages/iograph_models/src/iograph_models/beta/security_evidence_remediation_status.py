from __future__ import annotations
from enum import StrEnum


class SecurityEvidenceRemediationStatus(StrEnum):
	none = "none"
	remediated = "remediated"
	prevented = "prevented"
	blocked = "blocked"
	notFound = "notFound"
	unknownFutureValue = "unknownFutureValue"
	active = "active"
	pendingApproval = "pendingApproval"
	declined = "declined"
	unremediated = "unremediated"
	running = "running"
	partiallyRemediated = "partiallyRemediated"

