from __future__ import annotations
from enum import StrEnum


class SharingDomainRestrictionMode(StrEnum):
	none = "none"
	allowList = "allowList"
	blockList = "blockList"
	unknownFutureValue = "unknownFutureValue"

