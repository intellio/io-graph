from __future__ import annotations
from enum import StrEnum


class GroundingEntityType(StrEnum):
	site = "site"
	list = "list"
	listItem = "listItem"
	drive = "drive"
	driveItem = "driveItem"
	unknownFutureValue = "unknownFutureValue"

