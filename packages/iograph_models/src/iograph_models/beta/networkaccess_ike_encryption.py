from __future__ import annotations
from enum import StrEnum


class NetworkaccessIkeEncryption(StrEnum):
	aes128 = "aes128"
	aes192 = "aes192"
	aes256 = "aes256"
	gcmAes128 = "gcmAes128"
	gcmAes256 = "gcmAes256"
	unknownFutureValue = "unknownFutureValue"

