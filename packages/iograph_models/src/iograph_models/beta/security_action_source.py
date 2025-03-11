from __future__ import annotations
from enum import StrEnum


class SecurityActionSource(StrEnum):
	manual = "manual"
	automatic = "automatic"
	recommended = "recommended"
	default = "default"

