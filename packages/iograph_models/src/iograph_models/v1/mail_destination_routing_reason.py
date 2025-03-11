from __future__ import annotations
from enum import StrEnum


class MailDestinationRoutingReason(StrEnum):
	none = "none"
	mailFlowRule = "mailFlowRule"
	safeSender = "safeSender"
	blockedSender = "blockedSender"
	advancedSpamFiltering = "advancedSpamFiltering"
	domainAllowList = "domainAllowList"
	domainBlockList = "domainBlockList"
	notInAddressBook = "notInAddressBook"
	firstTimeSender = "firstTimeSender"
	autoPurgeToInbox = "autoPurgeToInbox"
	autoPurgeToJunk = "autoPurgeToJunk"
	autoPurgeToDeleted = "autoPurgeToDeleted"
	outbound = "outbound"
	notJunk = "notJunk"
	junk = "junk"
	unknownFutureValue = "unknownFutureValue"

