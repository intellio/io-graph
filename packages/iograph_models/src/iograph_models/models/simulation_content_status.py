from __future__ import annotations
from enum import Enum


class SimulationContentStatus(Enum):
	unknown = "unknown"
	draft = "draft"
	ready = "ready"
	archive = "archive"
	delete = "delete"
	unknownFutureValue = "unknownFutureValue"

