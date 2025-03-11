from __future__ import annotations
from enum import StrEnum


class SecurityAssignmentMethod(StrEnum):
	standard = "standard"
	privileged = "privileged"
	auto = "auto"

