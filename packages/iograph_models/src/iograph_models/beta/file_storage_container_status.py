from __future__ import annotations
from enum import StrEnum


class FileStorageContainerStatus(StrEnum):
	inactive = "inactive"
	active = "active"
	unknownFutureValue = "unknownFutureValue"

