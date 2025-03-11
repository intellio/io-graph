from __future__ import annotations
from enum import StrEnum


class NetworkaccessIkeIntegrity(StrEnum):
	sha256 = "sha256"
	sha384 = "sha384"
	gcmAes128 = "gcmAes128"
	gcmAes256 = "gcmAes256"
	unknownFutureValue = "unknownFutureValue"

