from __future__ import annotations
from enum import StrEnum


class AndroidWorkProfileAccountUse(StrEnum):
	allowAllExceptGoogleAccounts = "allowAllExceptGoogleAccounts"
	blockAll = "blockAll"
	allowAll = "allowAll"
	unknownFutureValue = "unknownFutureValue"

