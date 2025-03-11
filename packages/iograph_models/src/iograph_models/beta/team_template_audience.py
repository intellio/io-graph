from __future__ import annotations
from enum import StrEnum


class TeamTemplateAudience(StrEnum):
	organization = "organization"
	user = "user"
	public = "public"
	unknownFutureValue = "unknownFutureValue"

