from __future__ import annotations
from enum import Enum


class LocationUniqueIdType(Enum):
	unknown = "unknown"
	locationStore = "locationStore"
	directory = "directory"
	private = "private"
	bing = "bing"

