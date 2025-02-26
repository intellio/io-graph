from __future__ import annotations
from enum import Enum


class ConditionalAccessTransferMethods(Enum):
	none = "none"
	deviceCodeFlow = "deviceCodeFlow"
	authenticationTransfer = "authenticationTransfer"
	unknownFutureValue = "unknownFutureValue"

