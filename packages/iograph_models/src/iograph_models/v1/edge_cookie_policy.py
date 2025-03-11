from __future__ import annotations
from enum import StrEnum


class EdgeCookiePolicy(StrEnum):
	userDefined = "userDefined"
	allow = "allow"
	blockThirdParty = "blockThirdParty"
	blockAll = "blockAll"

