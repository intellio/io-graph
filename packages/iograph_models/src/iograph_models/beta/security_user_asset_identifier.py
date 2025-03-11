from __future__ import annotations
from enum import StrEnum


class SecurityUserAssetIdentifier(StrEnum):
	accountObjectId = "accountObjectId"
	accountSid = "accountSid"
	accountUpn = "accountUpn"
	accountName = "accountName"
	accountDomain = "accountDomain"
	accountId = "accountId"
	requestAccountSid = "requestAccountSid"
	requestAccountName = "requestAccountName"
	requestAccountDomain = "requestAccountDomain"
	recipientObjectId = "recipientObjectId"
	processAccountObjectId = "processAccountObjectId"
	initiatingAccountSid = "initiatingAccountSid"
	initiatingProcessAccountUpn = "initiatingProcessAccountUpn"
	initiatingAccountName = "initiatingAccountName"
	initiatingAccountDomain = "initiatingAccountDomain"
	servicePrincipalId = "servicePrincipalId"
	servicePrincipalName = "servicePrincipalName"
	targetAccountUpn = "targetAccountUpn"
	unknownFutureValue = "unknownFutureValue"

