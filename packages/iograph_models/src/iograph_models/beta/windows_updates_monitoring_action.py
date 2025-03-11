from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesMonitoringAction(StrEnum):
	alertError = "alertError"
	offerFallback = "offerFallback"
	pauseDeployment = "pauseDeployment"
	unknownFutureValue = "unknownFutureValue"

