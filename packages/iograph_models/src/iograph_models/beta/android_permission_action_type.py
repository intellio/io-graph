from __future__ import annotations
from enum import StrEnum


class AndroidPermissionActionType(StrEnum):
	prompt = "prompt"
	autoGrant = "autoGrant"
	autoDeny = "autoDeny"

