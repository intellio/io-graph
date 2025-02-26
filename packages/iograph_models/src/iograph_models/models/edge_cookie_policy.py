from __future__ import annotations
from enum import Enum


class EdgeCookiePolicy(Enum):
	userDefined = "userDefined"
	allow = "allow"
	blockThirdParty = "blockThirdParty"
	blockAll = "blockAll"

