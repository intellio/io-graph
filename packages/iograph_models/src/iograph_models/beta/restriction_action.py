from __future__ import annotations
from enum import StrEnum


class RestrictionAction(StrEnum):
	warn = "warn"
	audit = "audit"
	block = "block"

