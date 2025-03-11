from __future__ import annotations
from enum import StrEnum


class IdentityProviderState(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

