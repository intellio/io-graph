from __future__ import annotations
from enum import StrEnum


class AppLogDecryptionAlgorithm(StrEnum):
	aes256 = "aes256"
	unknownFutureValue = "unknownFutureValue"

