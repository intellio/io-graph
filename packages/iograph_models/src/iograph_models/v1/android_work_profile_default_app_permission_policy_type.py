from __future__ import annotations
from enum import StrEnum


class AndroidWorkProfileDefaultAppPermissionPolicyType(StrEnum):
	deviceDefault = "deviceDefault"
	prompt = "prompt"
	autoGrant = "autoGrant"
	autoDeny = "autoDeny"

