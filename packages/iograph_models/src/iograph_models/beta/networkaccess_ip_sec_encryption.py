from __future__ import annotations
from enum import StrEnum


class NetworkaccessIpSecEncryption(StrEnum):
	none = "none"
	gcmAes128 = "gcmAes128"
	gcmAes192 = "gcmAes192"
	gcmAes256 = "gcmAes256"
	unknownFutureValue = "unknownFutureValue"

