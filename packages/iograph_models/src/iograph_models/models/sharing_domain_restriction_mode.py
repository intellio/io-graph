from __future__ import annotations
from enum import Enum


class SharingDomainRestrictionMode(Enum):
	none = "none"
	allowList = "allowList"
	blockList = "blockList"
	unknownFutureValue = "unknownFutureValue"

