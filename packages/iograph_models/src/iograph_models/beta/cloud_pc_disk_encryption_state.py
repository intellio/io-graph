from __future__ import annotations
from enum import StrEnum


class CloudPcDiskEncryptionState(StrEnum):
	notAvailable = "notAvailable"
	notEncrypted = "notEncrypted"
	encryptedUsingPlatformManagedKey = "encryptedUsingPlatformManagedKey"
	encryptedUsingCustomerManagedKey = "encryptedUsingCustomerManagedKey"
	unknownFutureValue = "unknownFutureValue"

