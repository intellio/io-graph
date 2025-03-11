from __future__ import annotations
from enum import StrEnum


class FileVaultState(StrEnum):
	success = "success"
	driveEncryptedByUser = "driveEncryptedByUser"
	userDeferredEncryption = "userDeferredEncryption"
	escrowNotEnabled = "escrowNotEnabled"

