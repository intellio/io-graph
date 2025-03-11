from __future__ import annotations
from enum import StrEnum


class MessageEventType(StrEnum):
	received = "received"
	sent = "sent"
	delivered = "delivered"
	failed = "failed"
	processingFailed = "processingFailed"
	distributionGroupExpanded = "distributionGroupExpanded"
	submitted = "submitted"
	delayed = "delayed"
	redirected = "redirected"
	resolved = "resolved"
	dropped = "dropped"
	recipientsAdded = "recipientsAdded"
	malwareDetected = "malwareDetected"
	malwareDetectedInMessage = "malwareDetectedInMessage"
	malwareDetectedInAttachment = "malwareDetectedInAttachment"
	ttZapped = "ttZapped"
	ttDelivered = "ttDelivered"
	spamDetected = "spamDetected"
	transportRuleTriggered = "transportRuleTriggered"
	dlpRuleTriggered = "dlpRuleTriggered"
	journaled = "journaled"
	unknownFutureValue = "unknownFutureValue"

