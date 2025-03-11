from __future__ import annotations
from enum import StrEnum


class NetworkaccessAlgorithm(StrEnum):
	md5 = "md5"
	sha1 = "sha1"
	sha256 = "sha256"
	sha256ac = "sha256ac"
	unknownFutureValue = "unknownFutureValue"

