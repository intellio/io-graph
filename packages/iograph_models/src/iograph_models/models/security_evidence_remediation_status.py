from __future__ import annotations
from enum import Enum


class SecurityEvidenceRemediationStatus(Enum):
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

