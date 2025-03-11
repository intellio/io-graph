from __future__ import annotations
from enum import StrEnum


class WindowsDefenderProductStatus(StrEnum):
	noStatus = "noStatus"
	serviceNotRunning = "serviceNotRunning"
	serviceStartedWithoutMalwareProtection = "serviceStartedWithoutMalwareProtection"
	pendingFullScanDueToThreatAction = "pendingFullScanDueToThreatAction"
	pendingRebootDueToThreatAction = "pendingRebootDueToThreatAction"
	pendingManualStepsDueToThreatAction = "pendingManualStepsDueToThreatAction"
	avSignaturesOutOfDate = "avSignaturesOutOfDate"
	asSignaturesOutOfDate = "asSignaturesOutOfDate"
	noQuickScanHappenedForSpecifiedPeriod = "noQuickScanHappenedForSpecifiedPeriod"
	noFullScanHappenedForSpecifiedPeriod = "noFullScanHappenedForSpecifiedPeriod"
	systemInitiatedScanInProgress = "systemInitiatedScanInProgress"
	systemInitiatedCleanInProgress = "systemInitiatedCleanInProgress"
	samplesPendingSubmission = "samplesPendingSubmission"
	productRunningInEvaluationMode = "productRunningInEvaluationMode"
	productRunningInNonGenuineMode = "productRunningInNonGenuineMode"
	productExpired = "productExpired"
	offlineScanRequired = "offlineScanRequired"
	serviceShutdownAsPartOfSystemShutdown = "serviceShutdownAsPartOfSystemShutdown"
	threatRemediationFailedCritically = "threatRemediationFailedCritically"
	threatRemediationFailedNonCritically = "threatRemediationFailedNonCritically"
	noStatusFlagsSet = "noStatusFlagsSet"
	platformOutOfDate = "platformOutOfDate"
	platformUpdateInProgress = "platformUpdateInProgress"
	platformAboutToBeOutdated = "platformAboutToBeOutdated"
	signatureOrPlatformEndOfLifeIsPastOrIsImpending = "signatureOrPlatformEndOfLifeIsPastOrIsImpending"
	windowsSModeSignaturesInUseOnNonWin10SInstall = "windowsSModeSignaturesInUseOnNonWin10SInstall"

