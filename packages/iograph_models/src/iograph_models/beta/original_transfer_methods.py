from __future__ import annotations
from enum import StrEnum


class OriginalTransferMethods(StrEnum):
	none = "none"
	deviceCodeFlow = "deviceCodeFlow"
	authenticationTransfer = "authenticationTransfer"
	unknownFutureValue = "unknownFutureValue"

