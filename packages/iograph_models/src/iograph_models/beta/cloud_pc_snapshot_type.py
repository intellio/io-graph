from __future__ import annotations
from enum import StrEnum


class CloudPcSnapshotType(StrEnum):
	automatic = "automatic"
	manual = "manual"
	unknownFutureValue = "unknownFutureValue"

