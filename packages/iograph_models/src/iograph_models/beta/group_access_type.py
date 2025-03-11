from __future__ import annotations
from enum import StrEnum


class GroupAccessType(StrEnum):
	none = "none"
	private = "private"
	secret = "secret"
	public = "public"

