from __future__ import annotations
from enum import StrEnum


class GroupPrivacy(StrEnum):
	unspecified = "unspecified"
	public = "public"
	private = "private"
	unknownFutureValue = "unknownFutureValue"

