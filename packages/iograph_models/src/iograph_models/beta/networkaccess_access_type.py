from __future__ import annotations
from enum import StrEnum


class NetworkaccessAccessType(StrEnum):
	quickAccess = "quickAccess"
	privateAccess = "privateAccess"
	unknownFutureValue = "unknownFutureValue"
	appAccess = "appAccess"

