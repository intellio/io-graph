from __future__ import annotations
from enum import Enum


class MailDestinationRoutingReason(Enum):
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

