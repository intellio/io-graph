from __future__ import annotations
from enum import StrEnum


class ConditionalAccessTransferMethods(StrEnum):
	none = "none"
	deviceCodeFlow = "deviceCodeFlow"
	authenticationTransfer = "authenticationTransfer"
	unknownFutureValue = "unknownFutureValue"

