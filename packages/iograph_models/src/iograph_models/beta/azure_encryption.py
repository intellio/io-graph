from __future__ import annotations
from enum import StrEnum


class AzureEncryption(StrEnum):
	microsoftStorage = "microsoftStorage"
	microsoftKeyVault = "microsoftKeyVault"
	customer = "customer"
	unknownFutureValue = "unknownFutureValue"

