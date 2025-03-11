from __future__ import annotations
from enum import StrEnum


class ComanagementEligibleType(StrEnum):
	comanaged = "comanaged"
	eligible = "eligible"
	eligibleButNotAzureAdJoined = "eligibleButNotAzureAdJoined"
	needsOsUpdate = "needsOsUpdate"
	ineligible = "ineligible"
	scheduledForEnrollment = "scheduledForEnrollment"
	unknownFutureValue = "unknownFutureValue"

