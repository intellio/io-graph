from __future__ import annotations
from enum import StrEnum


class X509CertificateAffinityLevel(StrEnum):
	low = "low"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

