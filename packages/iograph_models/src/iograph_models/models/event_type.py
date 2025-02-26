from __future__ import annotations
from enum import Enum


class EventType(Enum):
	singleInstance = "singleInstance"
	occurrence = "occurrence"
	exception = "exception"
	seriesMaster = "seriesMaster"

