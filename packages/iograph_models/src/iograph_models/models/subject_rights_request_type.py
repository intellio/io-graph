from __future__ import annotations
from enum import Enum


class SubjectRightsRequestType(Enum):
	export = "export"
	delete = "delete"
	access = "access"
	tagForAction = "tagForAction"
	unknownFutureValue = "unknownFutureValue"

