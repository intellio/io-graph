from __future__ import annotations
from enum import StrEnum


class PlannerCreationSourceKind(StrEnum):
	none = "none"
	external = "external"
	publication = "publication"
	unknownFutureValue = "unknownFutureValue"

