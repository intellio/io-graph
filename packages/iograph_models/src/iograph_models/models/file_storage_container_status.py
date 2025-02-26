from __future__ import annotations
from enum import Enum


class FileStorageContainerStatus(Enum):
	inactive = "inactive"
	active = "active"
	unknownFutureValue = "unknownFutureValue"

