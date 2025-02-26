from __future__ import annotations
from enum import Enum


class SecurityAdditionalOptions(Enum):
	none = "none"
	teamsAndYammerConversations = "teamsAndYammerConversations"
	cloudAttachments = "cloudAttachments"
	allDocumentVersions = "allDocumentVersions"
	subfolderContents = "subfolderContents"
	listAttachments = "listAttachments"
	unknownFutureValue = "unknownFutureValue"

