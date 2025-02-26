from __future__ import annotations
from enum import Enum


class ChangeType(Enum):
	created = "created"
	updated = "updated"
	deleted = "deleted"

