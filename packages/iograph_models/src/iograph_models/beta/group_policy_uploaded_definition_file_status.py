from __future__ import annotations
from enum import StrEnum


class GroupPolicyUploadedDefinitionFileStatus(StrEnum):
	none = "none"
	uploadInProgress = "uploadInProgress"
	available = "available"
	assigned = "assigned"
	removalInProgress = "removalInProgress"
	uploadFailed = "uploadFailed"
	removalFailed = "removalFailed"

