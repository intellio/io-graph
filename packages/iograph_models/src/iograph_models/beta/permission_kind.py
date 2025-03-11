from __future__ import annotations
from enum import StrEnum


class PermissionKind(StrEnum):
	all = "all"
	enumerated = "enumerated"
	allPermissionsOnResourceApp = "allPermissionsOnResourceApp"
	unknownFutureValue = "unknownFutureValue"

