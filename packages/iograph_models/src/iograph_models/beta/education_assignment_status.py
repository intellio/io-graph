from __future__ import annotations
from enum import StrEnum


class EducationAssignmentStatus(StrEnum):
	draft = "draft"
	published = "published"
	assigned = "assigned"
	unknownFutureValue = "unknownFutureValue"
	inactive = "inactive"

