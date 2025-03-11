from __future__ import annotations
from enum import StrEnum


class VpnServerCertificateType(StrEnum):
	rsa = "rsa"
	ecdsa256 = "ecdsa256"
	ecdsa384 = "ecdsa384"
	ecdsa521 = "ecdsa521"

