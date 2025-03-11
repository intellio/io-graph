from __future__ import annotations
from enum import StrEnum


class ServiceStartType(StrEnum):
	manual = "manual"
	automatic = "automatic"
	disabled = "disabled"

