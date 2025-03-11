from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesDeploymentStateReasonValue(StrEnum):
	scheduledByOfferWindow = "scheduledByOfferWindow"
	offeringByRequest = "offeringByRequest"
	pausedByRequest = "pausedByRequest"
	pausedByMonitoring = "pausedByMonitoring"
	unknownFutureValue = "unknownFutureValue"
	faultedByContentOutdated = "faultedByContentOutdated"

