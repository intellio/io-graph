from __future__ import annotations
from enum import StrEnum


class X509CertificateAuthenticationMode(StrEnum):
	x509CertificateSingleFactor = "x509CertificateSingleFactor"
	x509CertificateMultiFactor = "x509CertificateMultiFactor"
	unknownFutureValue = "unknownFutureValue"

