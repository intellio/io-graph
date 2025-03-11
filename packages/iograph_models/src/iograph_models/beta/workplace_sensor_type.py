from __future__ import annotations
from enum import StrEnum


class WorkplaceSensorType(StrEnum):
	occupancy = "occupancy"
	peopleCount = "peopleCount"
	inferredOccupancy = "inferredOccupancy"
	heartbeat = "heartbeat"
	badge = "badge"
	unknownFutureValue = "unknownFutureValue"

