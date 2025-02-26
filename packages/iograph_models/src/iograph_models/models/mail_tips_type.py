from __future__ import annotations
from enum import Enum


class MailTipsType(Enum):
	automaticReplies = "automaticReplies"
	mailboxFullStatus = "mailboxFullStatus"
	customMailTip = "customMailTip"
	externalMemberCount = "externalMemberCount"
	totalMemberCount = "totalMemberCount"
	maxMessageSize = "maxMessageSize"
	deliveryRestriction = "deliveryRestriction"
	moderationStatus = "moderationStatus"
	recipientScope = "recipientScope"
	recipientSuggestions = "recipientSuggestions"

