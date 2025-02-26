from __future__ import annotations
from enum import Enum


class AndroidWorkProfileDefaultAppPermissionPolicyType(Enum):
	deviceDefault = "deviceDefault"
	prompt = "prompt"
	autoGrant = "autoGrant"
	autoDeny = "autoDeny"

