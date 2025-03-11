from __future__ import annotations
from enum import StrEnum


class SubjectRightsRequestType(StrEnum):
	export = "export"
	delete = "delete"
	access = "access"
	tagForAction = "tagForAction"
	unknownFutureValue = "unknownFutureValue"

