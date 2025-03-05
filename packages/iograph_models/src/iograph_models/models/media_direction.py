from __future__ import annotations
from enum import StrEnum


class MediaDirection(StrEnum):
	inactive = "inactive"
	sendOnly = "sendOnly"
	receiveOnly = "receiveOnly"
	sendReceive = "sendReceive"

