from __future__ import annotations
from enum import StrEnum


class SecurityTenantAllowBlockListAction(StrEnum):
	allow = "allow"
	block = "block"
	unknownFutureValue = "unknownFutureValue"

