from __future__ import annotations
from enum import StrEnum


class ApplicationPermissionsRequired(StrEnum):
	unknown = "unknown"
	anonymous = "anonymous"
	guest = "guest"
	user = "user"
	administrator = "administrator"
	system = "system"
	unknownFutureValue = "unknownFutureValue"

