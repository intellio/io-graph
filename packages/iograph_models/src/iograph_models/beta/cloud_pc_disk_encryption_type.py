from __future__ import annotations
from enum import StrEnum


class CloudPcDiskEncryptionType(StrEnum):
	platformManagedKey = "platformManagedKey"
	customerManagedKey = "customerManagedKey"
	unknownFutureValue = "unknownFutureValue"

