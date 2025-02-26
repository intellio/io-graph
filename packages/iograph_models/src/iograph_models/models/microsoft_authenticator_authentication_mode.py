from __future__ import annotations
from enum import Enum


class MicrosoftAuthenticatorAuthenticationMode(Enum):
	deviceBasedPush = "deviceBasedPush"
	push = "push"
	any = "any"

