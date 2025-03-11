from __future__ import annotations
from enum import StrEnum


class DataCollectionStatus(StrEnum):
	online = "online"
	offline = "offline"
	unknownFutureValue = "unknownFutureValue"

