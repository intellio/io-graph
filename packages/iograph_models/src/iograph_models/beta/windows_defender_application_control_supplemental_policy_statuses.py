from __future__ import annotations
from enum import StrEnum


class WindowsDefenderApplicationControlSupplementalPolicyStatuses(StrEnum):
	unknown = "unknown"
	success = "success"
	tokenError = "tokenError"
	notAuthorizedByToken = "notAuthorizedByToken"
	policyNotFound = "policyNotFound"

