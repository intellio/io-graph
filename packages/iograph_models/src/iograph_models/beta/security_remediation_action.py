from __future__ import annotations
from enum import StrEnum


class SecurityRemediationAction(StrEnum):
	moveToJunk = "moveToJunk"
	moveToInbox = "moveToInbox"
	hardDelete = "hardDelete"
	softDelete = "softDelete"
	moveToDeletedItems = "moveToDeletedItems"
	unknownFutureValue = "unknownFutureValue"

