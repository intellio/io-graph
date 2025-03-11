from __future__ import annotations
from enum import StrEnum


class GroupPolicyOperationType(StrEnum):
	none = "none"
	upload = "upload"
	uploadNewVersion = "uploadNewVersion"
	addLanguageFiles = "addLanguageFiles"
	removeLanguageFiles = "removeLanguageFiles"
	updateLanguageFiles = "updateLanguageFiles"
	remove = "remove"

