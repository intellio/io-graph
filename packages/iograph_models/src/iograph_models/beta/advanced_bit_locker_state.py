from __future__ import annotations
from enum import StrEnum


class AdvancedBitLockerState(StrEnum):
	success = "success"
	noUserConsent = "noUserConsent"
	osVolumeUnprotected = "osVolumeUnprotected"
	osVolumeTpmRequired = "osVolumeTpmRequired"
	osVolumeTpmOnlyRequired = "osVolumeTpmOnlyRequired"
	osVolumeTpmPinRequired = "osVolumeTpmPinRequired"
	osVolumeTpmStartupKeyRequired = "osVolumeTpmStartupKeyRequired"
	osVolumeTpmPinStartupKeyRequired = "osVolumeTpmPinStartupKeyRequired"
	osVolumeEncryptionMethodMismatch = "osVolumeEncryptionMethodMismatch"
	recoveryKeyBackupFailed = "recoveryKeyBackupFailed"
	fixedDriveNotEncrypted = "fixedDriveNotEncrypted"
	fixedDriveEncryptionMethodMismatch = "fixedDriveEncryptionMethodMismatch"
	loggedOnUserNonAdmin = "loggedOnUserNonAdmin"
	windowsRecoveryEnvironmentNotConfigured = "windowsRecoveryEnvironmentNotConfigured"
	tpmNotAvailable = "tpmNotAvailable"
	tpmNotReady = "tpmNotReady"
	networkError = "networkError"

