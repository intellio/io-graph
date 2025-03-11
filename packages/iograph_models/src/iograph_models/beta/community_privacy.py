from __future__ import annotations
from enum import StrEnum


class CommunityPrivacy(StrEnum):
	public = "public"
	private = "private"
	unknownFutureValue = "unknownFutureValue"

