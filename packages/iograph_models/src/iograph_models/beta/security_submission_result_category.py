from __future__ import annotations
from enum import StrEnum


class SecuritySubmissionResultCategory(StrEnum):
	notJunk = "notJunk"
	spam = "spam"
	phishing = "phishing"
	malware = "malware"
	allowedByPolicy = "allowedByPolicy"
	blockedByPolicy = "blockedByPolicy"
	spoof = "spoof"
	unknown = "unknown"
	noResultAvailable = "noResultAvailable"
	unknownFutureValue = "unknownFutureValue"
	beingAnalyzed = "beingAnalyzed"
	notSubmittedToMicrosoft = "notSubmittedToMicrosoft"
	phishingSimulation = "phishingSimulation"
	allowedDueToOrganizationOverride = "allowedDueToOrganizationOverride"
	blockedDueToOrganizationOverride = "blockedDueToOrganizationOverride"
	allowedDueToUserOverride = "allowedDueToUserOverride"
	blockedDueToUserOverride = "blockedDueToUserOverride"
	itemNotfound = "itemNotfound"
	threatsFound = "threatsFound"
	noThreatsFound = "noThreatsFound"
	domainImpersonation = "domainImpersonation"
	userImpersonation = "userImpersonation"
	brandImpersonation = "brandImpersonation"
	authenticationFailure = "authenticationFailure"
	spoofedBlocked = "spoofedBlocked"
	spoofedAllowed = "spoofedAllowed"
	reasonLostInTransit = "reasonLostInTransit"
	bulk = "bulk"

