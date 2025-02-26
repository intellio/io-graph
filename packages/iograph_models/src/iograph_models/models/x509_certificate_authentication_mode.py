from __future__ import annotations
from enum import Enum


class X509CertificateAuthenticationMode(Enum):
	x509CertificateSingleFactor = "x509CertificateSingleFactor"
	x509CertificateMultiFactor = "x509CertificateMultiFactor"
	unknownFutureValue = "unknownFutureValue"

