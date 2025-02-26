from __future__ import annotations
from enum import Enum


class AttendeeType(Enum):
	required = "required"
	optional = "optional"
	resource = "resource"

