from __future__ import annotations
from enum import StrEnum


class TeamVisibilityType(StrEnum):
	private = "private"
	public = "public"
	hiddenMembership = "hiddenMembership"
	unknownFutureValue = "unknownFutureValue"

