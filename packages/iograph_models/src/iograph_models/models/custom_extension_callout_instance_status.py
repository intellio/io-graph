from __future__ import annotations
from enum import StrEnum


class CustomExtensionCalloutInstanceStatus(StrEnum):
	calloutSent = "calloutSent"
	callbackReceived = "callbackReceived"
	calloutFailed = "calloutFailed"
	callbackTimedOut = "callbackTimedOut"
	waitingForCallback = "waitingForCallback"
	unknownFutureValue = "unknownFutureValue"

