from __future__ import annotations
from enum import StrEnum


class MailTipsType(StrEnum):
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

