from __future__ import annotations
from enum import StrEnum


class SecurityMailboxAssetIdentifier(StrEnum):
	accountUpn = "accountUpn"
	fileOwnerUpn = "fileOwnerUpn"
	initiatingProcessAccountUpn = "initiatingProcessAccountUpn"
	lastModifyingAccountUpn = "lastModifyingAccountUpn"
	targetAccountUpn = "targetAccountUpn"
	senderFromAddress = "senderFromAddress"
	senderDisplayName = "senderDisplayName"
	recipientEmailAddress = "recipientEmailAddress"
	senderMailFromAddress = "senderMailFromAddress"
	unknownFutureValue = "unknownFutureValue"

