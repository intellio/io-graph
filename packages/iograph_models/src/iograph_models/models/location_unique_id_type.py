from __future__ import annotations
from enum import StrEnum


class LocationUniqueIdType(StrEnum):
	unknown = "unknown"
	locationStore = "locationStore"
	directory = "directory"
	private = "private"
	bing = "bing"

