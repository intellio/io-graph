from __future__ import annotations
from enum import StrEnum


class NetworkaccessIpSecIntegrity(StrEnum):
	gcmAes128 = "gcmAes128"
	gcmAes192 = "gcmAes192"
	gcmAes256 = "gcmAes256"
	sha256 = "sha256"
	unknownFutureValue = "unknownFutureValue"

