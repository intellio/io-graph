from __future__ import annotations
from enum import StrEnum


class SecurityAdditionalOptions(StrEnum):
	none = "none"
	teamsAndYammerConversations = "teamsAndYammerConversations"
	cloudAttachments = "cloudAttachments"
	allDocumentVersions = "allDocumentVersions"
	subfolderContents = "subfolderContents"
	listAttachments = "listAttachments"
	unknownFutureValue = "unknownFutureValue"

