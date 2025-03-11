from __future__ import annotations
from enum import StrEnum


class SimulationContentStatus(StrEnum):
	unknown = "unknown"
	draft = "draft"
	ready = "ready"
	archive = "archive"
	delete = "delete"
	unknownFutureValue = "unknownFutureValue"

