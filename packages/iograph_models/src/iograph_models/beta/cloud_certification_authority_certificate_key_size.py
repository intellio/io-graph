from __future__ import annotations
from enum import StrEnum


class CloudCertificationAuthorityCertificateKeySize(StrEnum):
	unknown = "unknown"
	rsa2048 = "rsa2048"
	rsa3072 = "rsa3072"
	rsa4096 = "rsa4096"
	eCP256 = "eCP256"
	eCP256k = "eCP256k"
	eCP384 = "eCP384"
	eCP521 = "eCP521"
	unknownFutureValue = "unknownFutureValue"

