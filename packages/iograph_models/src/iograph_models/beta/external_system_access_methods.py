from __future__ import annotations
from enum import StrEnum


class ExternalSystemAccessMethods(StrEnum):
	direct = "direct"
	roleChaining = "roleChaining"
	unknownFutureValue = "unknownFutureValue"

