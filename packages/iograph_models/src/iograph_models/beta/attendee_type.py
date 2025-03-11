from __future__ import annotations
from enum import StrEnum


class AttendeeType(StrEnum):
	required = "required"
	optional = "optional"
	resource = "resource"

