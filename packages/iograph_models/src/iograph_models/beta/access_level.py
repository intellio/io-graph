from __future__ import annotations
from enum import StrEnum


class AccessLevel(StrEnum):
	everyone = "everyone"
	invited = "invited"
	locked = "locked"
	sameEnterprise = "sameEnterprise"
	sameEnterpriseAndFederated = "sameEnterpriseAndFederated"

