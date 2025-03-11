from __future__ import annotations
from enum import StrEnum


class ChangeType(StrEnum):
	created = "created"
	updated = "updated"
	deleted = "deleted"

