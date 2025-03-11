from __future__ import annotations
from enum import StrEnum


class MicrosoftAuthenticatorAuthenticationMode(StrEnum):
	deviceBasedPush = "deviceBasedPush"
	push = "push"
	any = "any"

