from __future__ import annotations
from enum import StrEnum


class SecurityAdditionalDataOptions(StrEnum):
	allVersions = "allVersions"
	linkedFiles = "linkedFiles"
	unknownFutureValue = "unknownFutureValue"
	advancedIndexing = "advancedIndexing"
	listAttachments = "listAttachments"
	htmlTranscripts = "htmlTranscripts"
	messageConversationExpansion = "messageConversationExpansion"
	locationsWithoutHits = "locationsWithoutHits"
	allItemsInFolder = "allItemsInFolder"

