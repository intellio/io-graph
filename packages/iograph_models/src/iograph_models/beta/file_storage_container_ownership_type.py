from __future__ import annotations
from enum import StrEnum


class FileStorageContainerOwnershipType(StrEnum):
	tenantOwned = "tenantOwned"
	userOwned = "userOwned"
	unknownFutureValue = "unknownFutureValue"

