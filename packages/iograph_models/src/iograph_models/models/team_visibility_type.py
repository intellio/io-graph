from __future__ import annotations
from enum import Enum


class TeamVisibilityType(Enum):
	private = "private"
	public = "public"
	hiddenMembership = "hiddenMembership"
	unknownFutureValue = "unknownFutureValue"

