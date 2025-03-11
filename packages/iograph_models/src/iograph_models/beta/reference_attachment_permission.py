from __future__ import annotations
from enum import StrEnum


class ReferenceAttachmentPermission(StrEnum):
	other = "other"
	view = "view"
	edit = "edit"
	anonymousView = "anonymousView"
	anonymousEdit = "anonymousEdit"
	organizationView = "organizationView"
	organizationEdit = "organizationEdit"

