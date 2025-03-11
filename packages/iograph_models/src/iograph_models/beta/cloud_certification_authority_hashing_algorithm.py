from __future__ import annotations
from enum import StrEnum


class CloudCertificationAuthorityHashingAlgorithm(StrEnum):
	unknown = "unknown"
	sha256 = "sha256"
	sha384 = "sha384"
	sha512 = "sha512"
	unknownFutureValue = "unknownFutureValue"

