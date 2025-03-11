from __future__ import annotations
from enum import StrEnum


class MacOSFileVaultRecoveryKeyTypes(StrEnum):
	notConfigured = "notConfigured"
	institutionalRecoveryKey = "institutionalRecoveryKey"
	personalRecoveryKey = "personalRecoveryKey"

