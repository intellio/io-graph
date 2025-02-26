from __future__ import annotations
from enum import Enum


class EducationAssignmentStatus(Enum):
	draft = "draft"
	published = "published"
	assigned = "assigned"
	unknownFutureValue = "unknownFutureValue"
	inactive = "inactive"

