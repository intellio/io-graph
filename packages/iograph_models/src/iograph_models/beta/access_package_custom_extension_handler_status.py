from __future__ import annotations
from enum import StrEnum


class AccessPackageCustomExtensionHandlerStatus(StrEnum):
	requestSent = "requestSent"
	requestReceived = "requestReceived"
	unknownFutureValue = "unknownFutureValue"

