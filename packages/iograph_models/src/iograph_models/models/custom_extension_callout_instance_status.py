from __future__ import annotations
from enum import Enum


class CustomExtensionCalloutInstanceStatus(Enum):
	calloutSent = "calloutSent"
	callbackReceived = "callbackReceived"
	calloutFailed = "calloutFailed"
	callbackTimedOut = "callbackTimedOut"
	waitingForCallback = "waitingForCallback"
	unknownFutureValue = "unknownFutureValue"

