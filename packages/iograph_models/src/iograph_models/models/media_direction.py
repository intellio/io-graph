from __future__ import annotations
from enum import Enum


class MediaDirection(Enum):
	inactive = "inactive"
	sendOnly = "sendOnly"
	receiveOnly = "receiveOnly"
	sendReceive = "sendReceive"

