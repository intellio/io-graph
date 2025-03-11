from __future__ import annotations
from enum import StrEnum


class EmailType(StrEnum):
	unknown = "unknown"
	work = "work"
	personal = "personal"
	main = "main"
	other = "other"

