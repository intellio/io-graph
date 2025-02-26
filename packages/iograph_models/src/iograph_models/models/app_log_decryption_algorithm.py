from __future__ import annotations
from enum import Enum


class AppLogDecryptionAlgorithm(Enum):
	aes256 = "aes256"
	unknownFutureValue = "unknownFutureValue"

