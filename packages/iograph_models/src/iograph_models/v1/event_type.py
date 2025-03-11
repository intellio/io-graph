from __future__ import annotations
from enum import StrEnum


class EventType(StrEnum):
	singleInstance = "singleInstance"
	occurrence = "occurrence"
	exception = "exception"
	seriesMaster = "seriesMaster"

